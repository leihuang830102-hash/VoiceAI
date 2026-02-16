"""
Zhipu GLM LLM Service (OpenAI Compatible)
智谱 GLM 大语言模型服务 - OpenAI 兼容接口
"""

import aiohttp
import json
from loguru import logger
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

ZHIPU_API_KEY = os.getenv("ZHIPU_API_KEY", "")
ZHIPU_BASE_URL = os.getenv("ZHIPU_BASE_URL", "https://open.bigmodel.cn/api/paas/v4/")
GLM_MODEL = os.getenv("GLM_MODEL", "glm-4")


class ZhipuGLMService:
    """Zhipu GLM LLM Service - OpenAI Compatible interface."""

    def __init__(self, api_key: str = None, model: str = "glm-4"):
        """Initialize Zhipu GLM LLM service.

        Args:
            api_key: Zhipu AI API key
            model: GLM model ID (default: glm-4)
        """
        self.api_key = api_key
        self.model = model
        logger.info(f"Initializing Zhipu GLM service with model: {model}")

    async def get_llm_config(self) -> dict:
        """Get LLM service configuration for RTVI."""
        # Zhipu GLM service configuration
        return [{
            "service": "llm",
            "options": [
                {"name": "model", "value": self.model}
            ]
        }]

    async def chat(self, messages: list, system_prompt: str = None) -> str:
        """Send chat request to LLM.

        Args:
            messages: Conversation messages
            system_prompt: System prompt

        Returns:
            LLM response text
        """
        logger.info(f"Sending chat request to Zhipu GLM...")
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        "X-Api-Resource-Id": "volc.bigmodel.cn",
            "X-Api-Request-Id": self._generate_request_id(),
        }

        data = {
            "model": self.model,
            "messages": messages,
        "stream": True,
        }

        try:
            async with aiohttp.ClientSession(headers=headers) as session:
                response = await session.post(
                    f"{ZHIPU_BASE_URL}/chat/completions",
                    json=data
                )

                if response.status == 200:
                    result = await response.json()
                    logger.success(f"Zhipu GLM chat successful")
                    return result.get("choices", [{}]).get("message", {}).get("content", "")
                else:
                    logger.error(f"Zhipu GLM chat failed: {response.status}")
                    raise Exception(f"Zhipu GLM chat error: {response.status}")
        except Exception as e:
            logger.error(f"Zhipu GLM chat exception: {e}")
            raise Exception(f"Zhipu GLM chat error: {e}")

    except Exception as e:
            logger.error(f"Zhipu GLM chat error: {e}")

    async def _generate_request_id(self) -> str:
        """Generate a unique request ID."""
        import uuid
        return str(uuid.uuid4())


# Singleton instance
_instance = None


def get_service() -> "ZhipuGLMService":
    """Get or create singleton instance of Zhipu GLM LLM Service."""
    global _instance
    if _instance is None:
        _instance = ZhipuGLMService()
    return _instance
