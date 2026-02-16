"""
RTVI Observer for VoiceAI
VoiceAI 的 RTVI 观察者
"""

from pipecat.processors.frame_processor import FrameProcessor
from pipecat.frames.frames import (
    UserStartedSpeakingFrame,
    UserStoppedSpeakingFrame,
    BotStartedSpeakingFrame,
    BotStoppedSpeakingFrame,
    LLMTextFrame,
    UserTranscriptionFrame,
    BotTranscriptionFrame,
)
from loguru import logger


class RTVIObserver:
    """RTVI Observer that monitors pipeline events and converts them to RTVI format."""

    def __init__(self, rtvi_processor):
        self.rtvi = rtvi_processor

    async def handle_frame(self, frame, direction):
        """Process incoming frames and send RTVI events."""
        if isinstance(frame, UserStartedSpeakingFrame):
            await self.rtvi.handle_event("user_started_speaking")

        elif isinstance(frame, UserStoppedSpeakingFrame):
            await self.rtvi.handle_event("user_stopped_speaking")

        elif isinstance(frame, BotStartedSpeakingFrame):
            await self.rtvi.handle_event("bot_started_speaking")

        elif isinstance(frame, BotStoppedSpeakingFrame):
            await self.rtvi.handle_event("bot_stopped_speaking")

        elif isinstance(frame, LLMTextFrame):
            await self.rtvi.handle_event("llm_text", text=frame.text)

        elif isinstance(frame, UserTranscriptionFrame):
            await self.rtvi.handle_event("user_transcription", text=frame.text)

        elif isinstance(frame, BotTranscriptionFrame):
            await self.rtvi.handle_event("bot_transcription", text=frame.text)
        else:
            logger.debug(f"Unhandled frame type: {type(frame)}")
