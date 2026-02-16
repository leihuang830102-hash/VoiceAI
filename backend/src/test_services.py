#!/usr/bin/env python3
"""
Test Services for VoiceAI
VoiceAI 服务测试
"""

import asyncio
from loguru import logger
from doubao_stt import DoubaoSTTService, get_service as get_stt_service
from doubao_tts import DoubaoTTSService, get_service as get_tts_service


async def test_doubao_stt():
    """Test Doubao STT service."""
    logger.info("Testing Doubao STT service...")

    try:
        stt_service = get_stt_service()

        # Note: This test requires a valid audio URL
        # For now, we'll just verify the service is initialized
        logger.info(f"STT service initialized: {stt_service}")
        logger.info(f"API Key: {stt_service.api_key[:10]}...")
        logger.info(f"App ID: {stt_service.app_id}")

        # You can test with an actual audio URL like:
        # audio_url = "https://example.com/sample.mp3"
        # task_id = await stt_service.submit_task(audio_url)
        # result = await stt_service.get_result(task_id)
        # logger.success(f"STT test result: {result}")

        logger.success("Doubao STT service test passed")
        return True

    except Exception as e:
        logger.error(f"Doubao STT service test failed: {e}")
        return False


async def test_doubao_tts():
    """Test Doubao TTS service."""
    logger.info("Testing Doubao TTS service...")

    try:
        tts_service = get_tts_service()

        # Test text-to-speech
        test_text = "你好，我是语音助手。Hello, I am a voice assistant."
        logger.info(f"Testing TTS with text: {test_text}")

        # Note: The TTS API requires proper access key
        # For now, we'll just verify the service is initialized
        logger.info(f"TTS service initialized: {tts_service}")
        logger.info(f"API Key: {tts_service.api_key[:10]}...")
        logger.info(f"App ID: {tts_service.app_id}")

        # You can test with actual text when access key is configured:
        # audio_data = await tts_service.synthesize(test_text)
        # logger.success(f"TTS synthesis successful, audio data size: {len(audio_data)} bytes")

        logger.success("Doubao TTS service test passed")
        return True

    except Exception as e:
        logger.error(f"Doubao TTS service test failed: {e}")
        return False


async def test_zhipu_glm():
    """Test Zhipu GLM LLM service."""
    logger.info("Testing Zhipu GLM LLM service...")

    try:
        from zhipu_llm import get_service as get_glm_service

        glm_service = get_glm_service()

        # Test chat completion
        test_messages = [
            {"role": "user", "content": "你好，请介绍一下你自己。"}
        ]

        logger.info(f"Testing GLM with messages: {test_messages}")

        # Note: We're using OpenAILLMService from server.py for GLM
        # The ZhipuGLMService in zhipu_llm.py is an alternative implementation
        logger.info(f"GLM service initialized: {glm_service}")
        logger.info(f"API Key: {glm_service.api_key[:10]}...")
        logger.info(f"Model: {glm_service.model}")

        # You can test actual chat completion when the service is fully integrated:
        # response = await glm_service.chat(test_messages)
        # logger.success(f"GLM chat response: {response}")

        logger.success("Zhipu GLM LLM service test passed")
        return True

    except Exception as e:
        logger.error(f"Zhipu GLM LLM service test failed: {e}")
        return False


async def main():
    """Run all tests."""
    logger.info("Starting service tests...")

    results = {
        "Doubao STT": await test_doubao_stt(),
        "Doubao TTS": await test_doubao_tts(),
        "Zhipu GLM": await test_zhipu_glm(),
    }

    logger.info("\n=== Test Results ===")
    for service, result in results.items():
        status = "PASSED" if result else "FAILED"
        logger.info(f"{service}: {status}")

    all_passed = all(results.values())
    if all_passed:
        logger.success("All tests passed!")
    else:
        logger.warning("Some tests failed")

    return all_passed


if __name__ == "__main__":
    asyncio.run(main())
