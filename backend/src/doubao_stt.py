"""
Doubao STT Service (Speech-to-Text)
豆包 STT 服务（语音转文字）
"""

import aiohttp
import json
import os
from dotenv import load_dotenv
from loguru import logger

# Load environment variables
load_dotenv()

DOUBAO_API_KEY = os.getenv("DOUBAO_API_KEY", "")
DOUBAO_APP_ID = os.getenv("DOUBAO_APP_ID", "25802508")
DOUBAO_ACCESS_KEY = os.getenv("DOUBAO_ACCESS_KEY", "")
DOUBAO_API_URL = "https://openspeech.bytedance.com/api/v3/auc/bigmodel/submit"


class DoubaoSTTService:
    """Doubao Speech-to-Text Service implementation."""

    def __init__(self):
        self.api_key = DOUBAO_API_KEY
        self.app_id = DOUBAO_APP_ID
        self.access_key = DOUBAO_ACCESS_KEY
        self.api_url = DOUBAO_API_URL

    async def submit_task(self, audio_url: str) -> str:
        """
        Submit audio file for recognition.
        提交音频文件获取任务 ID

        Args:
            audio_url: Audio file URL

        Returns:
            Task ID
        """
        logger.info(f"Submitting audio for recognition: {audio_url}")

        headers = {
            "Content-Type": "application/json",
            "X-Api-App-Key": self.app_id,
            "X-Api-Access-Key": self.access_key,
        "X-Api-Request-Id": self._generate_request_id(),
        "X-Api-Resource-Id": "volc.bigasr.auc",
            "X-Api-Sequence": "1",
        }

        data = {
            "app": {
                "audio": {
                    "url": audio_url,
                    "format": "mp3",
                    "language": "zh-CN",  # Chinese
                    "codec": "mp3",
                    "rate": 16000,
                    "bits": 16,
                    "channel": 1,
                    "enable_itn": False,
                    "enable_punc": False,
                    "enable_ddc": False,
                    "enable_speaker_info": False,
                    "enable_channel_split": False,
                    "enable_emotion_detection": False,
                    "enable_gender_detection": False,
                }
            },
            "uid": "38880818508",  # Use your own UID
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(self.api_url, json=data) as response:
                response_json = await response.json()
                logger.info(f"Submit task response: {response_json}")

                if response_json.get("code") == "20000000":
                    logger.info(f"Task submitted successfully, task ID: {response_json.get('task_id')}")
                    return response_json.get("task_id")

                else:
                    logger.error(f"Task submission failed: {response_json}")
                    raise Exception(f"Failed to submit audio task: {response_json}")

    async def get_result(self, task_id: str) -> dict:
        """
        Query recognition result by task ID.
        使用任务 ID 查询识别结果

        Args:
            task_id: Task ID returned from submit_task

        Returns:
            Recognition result dict
        """
        logger.info(f"Querying result for task: {task_id}")

        headers = {
            "Content-Type": "application/json",
            "X-Api-App-Key": self.app_id,
            "X-Api-Access-Key": self.access_key,
        "X-Api-Request-Id": self._generate_request_id(),
            "X-Api-Resource-Id": "volc.bigasr.auc",
            "X-Api-Sequence": "1",
        }

        data = {
            "app": {
                "task": task_id,
            "result": 0,  # Only need task, don't need result
            "format": "json",
                "language": "zh-CN",
            "enable_itn": False,
                "enable_punc": False,
                "enable_ddc": False,
            "enable_speaker_info": False,
                "enable_channel_split": False,
                "enable_emotion_detection": False,
                "enable_gender_detection": False,
            },
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(self.api_url, json=data) as response:
                response_json = await response.json()
                logger.debug(f"Query result response: {response_json}")

                if response_json.get("code") == "20000000":
                    result_data = response_json.get("result", {})

                    # Parse utterances
                    utterances = result_data.get("utterances", [])
                    transcriptions = []

                    for utterance in utterances:
                        text = utterance.get("text", "").strip()
                        if text:
                            transcriptions.append({
                                "text": text,
                                "utterance": utterance.get("utterance", 0),
                                "start_time": utterance.get("start_time", 0),
                                "end_time": utterance.get("end_time", 0),
                            })

                    # Combine all text into a single result
                    full_text = " ".join([u["text"] for u in transcriptions])

                    result = {
                        "text": full_text,
                        "utterances": transcriptions,
                    }
                else:
                    logger.error(f"Failed to query result: {response_json}")
                    raise Exception(f"Failed to query result: {response_json}")

                return result

    def _generate_request_id(self) -> str:
        """Generate a unique request ID."""
        import uuid
        return str(uuid.uuid4())

    async def transcribe(self, audio_url: str) -> str:
        """
        Transcribe audio file and return recognized text.
        转录音频并返回识别结果

        Args:
            audio_url: Audio file URL

        Returns:
            Recognized text
        """
        task_id = await self.submit_task(audio_url)
        result = await self.get_result(task_id)

        return result.get("text", "")


# Singleton instance
_instance = None


def get_service() -> "DoubaoSTTService":
    """Get or create the singleton instance of DoubaoSTTService."""
    global _instance
    if _instance is None:
        _instance = DoubaoSTTService()
    return _instance
