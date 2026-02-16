#!/usr/bin/env python3
"""
VoiceAI Server - Real-time voice AI assistant using Pipecat
VoiceAI 服务器 - 使用 Pipecat 的实时语音 AI 助手
"""

import os
from dotenv import load_dotenv
from loguru import logger
from pipecat.processors.frame_processor import FrameDirection
from pipecat.services.openai.llm import OpenAILLMService
from pipecat.services.ai_services import RTVAudioService, TTSService, LLMService

from rtvi.processor import RTVIProcessor, RTVIConfig
from rtvi.observer import RTVIObserver

# Load environment variables
load_dotenv()

# Determine which LLM provider to use
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "doubao").lower()

logger.info(f"Starting VoiceAI server with LLM provider: {LLM_PROVIDER}")


def get_llm_service() -> LLMService:
    """Get the configured LLM service based on environment variable."""
    if LLM_PROVIDER == "doubao":
        # Use Doubao LLM service
        # TODO: Implement Doubao LLM service
        raise NotImplementedError("Doubao LLM service not yet implemented")
    elif LLM_PROVIDER == "glm":
        # Use Zhipu GLM service (OpenAI Compatible)
        api_key = os.getenv("ZHIPU_API_KEY")
        base_url = os.getenv("ZHIPU_BASE_URL", "https://open.bigmodel.cn/api/paas/v4/")
        model = os.getenv("GLM_MODEL", "glm-4")

        logger.info(f"Initializing Zhipu GLM service with model: {model}")
        return OpenAILLMService(
            api_key=api_key,
            base_url=base_url,
            model=model,
        )
    else:
        raise ValueError(f"Unknown LLM provider: {LLM_PROVIDER}")


# Test endpoint for Doubao STT service
@app.get("/test/stt")
async def test_stt():
    """Test Doubao STT service."""
    logger.info("Testing Doubao STT service...")
    try:
        from ..doubao_stt import DoubaoSTTService
        # Test with a sample audio URL (TODO: Replace with actual audio URL)
        audio_url = "https://example.com/sample.mp3"

        stt_service = DoubaoSTTService()

        # Submit a test task
        task_id = await stt_service.submit_task(audio_url)
        logger.info(f"Test task submitted, ID: {task_id}")

        # Wait and query result
        await asyncio.sleep(5)  # Wait for processing

        result = await stt_service.get_result(task_id)

        if result:
            logger.success(f"STT test successful: {result}")
            return {"success": True, "text": result.get("text", "")}
        else:
            logger.error(f"STT test failed")
            return {"success": False, "error": "Failed to get result"}

    except Exception as e:
        logger.error(f"STT test error: {e}")
            return {"success": False, "error": str(e)}
    """Main entry point for VoiceAI server."""
    from pipecat.flows import Flow
    from pipecat.transports.daily import DailyTransport
    from pipecat.transports.services.transport import TransportSessionArgs
    from pipecat.services.openai import openai_realtime

    # Configure RTVI services
    rtvi_config = RTVIConfig(
        vad=RTVAudioService(),
        stt=None,  # Will use Doubao STT
        llm=get_llm_service(),
        tts=None,  # Will use Doubao TTS
    )

    # Create RTVI processor and observer
    rtvi = RTVIProcessor(config=rtvi_config)
    observer = RTVIObserver(rtvi)

    # Setup transport (using Daily for WebRTC)
    transport = DailyTransport(
        room_name=os.getenv("DAILY_ROOM", "voice-ai-room"),
        token=os.getenv("DAILY_API_KEY", ""),
        url=os.getenv("DAILY_URL", "wss://api.daily.co/v1/"),
        audio_enabled=True,
        video_enabled=False,
    )

    # Build the pipeline
    # transport.input() → rtvi → doubao_stt → llm → doubao_tts → transport.output()
    # rtvi_observer → client events

    @transport.event_handler("on_participant_connected")
    async def on_participant_connected(transport, participant):
        logger.info(f"Client connected: {participant.identity}")
        await rtvi.handle_event("client_ready")
        await rtvi.set_bot_ready()

    @transport.event_handler("on_participant_disconnected")
    async def on_participant_disconnected(transport, participant, reason):
        logger.info(f"Client disconnected: {participant.identity}, reason: {reason}")
        await rtvi.handle_event("bot_disconnected")

    await transport.start(TransportSessionArgs(room_name=os.getenv("DAILY_ROOM")))
    await rtvi.start()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
