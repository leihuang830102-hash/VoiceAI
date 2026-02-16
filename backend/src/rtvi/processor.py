"""
RTVI Processor for VoiceAI
VoiceAI 的 RTVI 处理器
"""

from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List
from pipecat.services.ai_services import TTSService, LLMService
from pipecat.frames.frames import (
    BotReadyFrame,
    ClientReadyFrame,
    ConfigFrame,
    ErrorFrame,
    UserStartedSpeakingFrame,
    UserStoppedSpeakingFrame,
    BotStartedSpeakingFrame,
    BotStoppedSpeakingFrame,
    LLMTextFrame,
    UserTranscriptionFrame,
    BotTranscriptionFrame,
)
from loguru import logger

# Import Doubao STT service
from ..doubao_stt import DoubaoSTTService, get_service as get_doubao_stt_service
# Import Zhipu GLM LLM service
from ..zhipu_llm import get_service as get_glm_llm_service


@dataclass
class RTVIConfig:
    """Configuration for RTVI processor."""
    stt: Optional[TTSService] = None
    llm: Optional[LLMService] = None
    tts: Optional[TTSService] = None


@dataclass
class RTVIProcessor:
    """RTVI Processor for handling client-server communication."""

    config: RTVIConfig
    _client_ready: bool = False
    _bot_ready: bool = False

    def __init__(self, config: RTVIConfig):
        """Initialize RTVI processor with configuration."""
        self.config = config
        self._client_ready = False
        self._bot_ready = False

    async def handle_event(self, event_name: str, **kwargs) -> None:
        """Handle RTVI events."""
        if event_name == "client_ready":
            self._client_ready = True
            logger.info("Client ready, sending bot_ready...")
            yield ClientReadyFrame()
        elif event_name == "bot_ready":
            self._bot_ready = True
            logger.info("Bot ready, sending config...")
            # Send configuration with LLM options and STT service
            config_data = self._get_llm_config()
            yield ConfigFrame(config=config_data)
        elif event_name == "user_started_speaking":
            logger.info("User started speaking")
            yield UserStartedSpeakingFrame()
        elif event_name == "user_stopped_speaking":
            logger.info("User stopped speaking")
            yield UserStoppedSpeakingFrame()
        elif event_name == "bot_started_speaking":
            logger.info("Bot started speaking")
            yield BotStartedSpeakingFrame()
        elif event_name == "bot_stopped_speaking":
            logger.info("Bot stopped speaking")
            yield BotStoppedSpeakingFrame()
        elif event_name == "user_transcription":
            logger.debug(f"User transcription: {kwargs}")
            yield UserTranscriptionFrame(**kwargs)
        elif event_name == "bot_transcription":
            logger.debug(f"Bot transcription: {kwargs}")
            yield BotTranscriptionFrame(**kwargs)
        elif event_name == "llm_text":
            logger.debug(f"LLM text: {kwargs}")
            yield LLMTextFrame(**kwargs)
        elif event_name == "error":
            logger.error(f"Error: {kwargs}")
            yield ErrorFrame(**kwargs)
        else:
            logger.warning(f"Unknown event: {event_name}")

    def _get_llm_config(self) -> List[Dict[str, Any]]:
        """Get LLM service configuration for RTVI."""
        config_data = []

        # Add Doubao STT service if configured
        if self.config.stt:
            config_data.append({
                "service": "doubao_stt",
                "options": []
            })

        # Add Zhipu GLM LLM service if configured
        if self.config.llm:
            # Check the model to determine service type
            model = getattr(self.config.llm, "model", "")
            if "glm" in model.lower() or model.startswith("glm"):
                # Zhipu GLM via OpenAI compatible
                config_data.append({
                    "service": "glm",
                    "options": [
                        {"name": "model", "value": model or "glm-4"},
                        {"name": "temperature", "value": 0.7},
                    ]
                })

        return config_data

    async def set_client_ready(self) -> None:
        """Mark client as ready."""
        self._client_ready = True

    async def set_bot_ready(self) -> None:
        """Mark bot as ready."""
        if self._client_ready:
            self._bot_ready = True
        else:
            logger.warning("Cannot set bot_ready: client not ready")