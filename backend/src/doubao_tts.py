"""
Doubao TTS Service (Text-to-Speech)
豆包 TTS 服务（文字转语音）
"""

import os
import aiohttp
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DOUBAO_API_KEY = os.getenv("DOUBAO_API_KEY", "")
DOUBAO_APP_ID = os.getenv("DOUBAO_APP_ID", "25802508")
DOUBAO_ACCESS_KEY = os.getenv("DOUBAO_ACCESS_KEY", "")
DOUBAO_TTS_URL = "https://openspeech.bytedance.com/api/v3/tts"


class DoubaoTTSService:
    """Doubao Text-to-Speech Service implementation."""

    def __init__(self):
        self.api_key = DOUBAO_API_KEY
        self.app_id = DOUBAO_APP_ID
        self.access_key = DOUBAO_ACCESS_KEY
        self.api_url = DOUBAO_TTS_URL

    async def synthesize(self, text: str, voice: str = "zh_female_qingxin") -> bytes:
        """
        Synthesize speech from text.
        将文字转换为语音

        Args:
            text: Text to synthesize
            voice: Voice type (default: zh_female_qingxin)

        Returns:
            Audio data as bytes
        """
        logger.info(f"Synthesizing speech for text: {text[:50]}...")

        headers = {
            "Content-Type": "application/json",
            "X-Api-App-Key": self.app_id,
            "X-Api-Access-Key": self.access_key,
            "X-Api-Request-Id": self._generate_request_id(),
            "X-Api-Resource-Id": "volc.tts",
            "X-Api-Sequence": "1",
        }

        data = {
            "app": {
                "appId": self.app_id,
                "token": self.access_key,
                "cluster": "volcano_tts",
            },
            "user": {
                "uid": "38880818508",  # Use your own UID
            },
            "audio": {
                "voice_type": voice,
                "encoding": "mp3",
                "speed_ratio": 1.0,
                "volume_ratio": 1.0,
                "pitch_ratio": 1.0,
            },
            "request": {
                "reqid": self._generate_request_id(),
                "text": text,
                "text_type": "plain",
                "operation": "submit",
            }
        }

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                async with session.post(self.api_url, json=data) as response:
                    response_json = await response.json()
                    logger.debug(f"TTS response: {response_json}")

                    if response_json.get("code") == "0" or response_json.get("code") == "20000000":
                        # Get the audio data URL or data
                        if "data" in response_json:
                            audio_data = response_json["data"]
                            logger.success(f"TTS synthesis successful")
                            return audio_data
                        elif "url" in response_json:
                            # Download audio from URL
                            audio_url = response_json["url"]
                            async with session.get(audio_url) as audio_response:
                                audio_data = await audio_response.read()
                                logger.success(f"TTS synthesis successful")
                                return audio_data
                        else:
                            logger.error(f"TTS response missing audio data: {response_json}")
                            raise Exception("TTS response missing audio data")
                    else:
                        logger.error(f"TTS synthesis failed: {response_json}")
                        raise Exception(f"TTS synthesis error: {response_json}")
        except Exception as e:
            logger.error(f"TTS synthesis exception: {e}")
            raise Exception(f"TTS synthesis error: {e}")

    def _generate_request_id(self) -> str:
        """Generate a unique request ID."""
        import uuid
        return str(uuid.uuid4())


# Singleton instance
_instance = None


def get_service() -> "DoubaoTTSService":
    """Get or create the singleton instance of DoubaoTTSService."""
    global _instance
    if _instance is None:
        _instance = DoubaoTTSService()
    return _instance
