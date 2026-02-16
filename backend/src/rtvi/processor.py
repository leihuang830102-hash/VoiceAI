"""
RTVI Processor for VoiceAI
VoiceAI 的 RTVI 处理器
"""

from dataclasses import dataclass, field
from typing import Optional, Any, Dict, List
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


@dataclass
class RTVIConfig:
    """Configuration for RTVI processor."""
    vad: RTVAudioService
    stt: Optional[TTSService]
    llm: Optional[LLMService]
    tts: Optional[TTSService]


@dataclass
class RTVIProcessor:
    """RTVI Processor for handling client-server communication."""

    config: RTVIConfig
    _client_ready: bool = False
    _bot_ready: bool = False

    async def handle_event(self, event_name: str, **kwargs) -> None:
        """Handle RTVI events."""
        if event_name == "client_ready":
            self._client_ready = True
            logger.info("Client ready, sending bot_ready...")
            yield ClientReadyFrame()
        elif event_name == "bot_ready":
            self._bot_ready = True
            logger.info("Bot ready, sending config...")
            # Send configuration with LLM options
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
        if self.config.llm:
            return [{"service": "llm", "options": []}]
        return []

    async def set_client_ready(self) -> None:
        """Mark client as ready."""
        self._client_ready = True

    async def set_bot_ready(self) -> None:
        """Mark bot as ready."""
        if self._client_ready:
            self._bot_ready = True
        else:
            logger.warning("Cannot set bot_ready: client not ready")
