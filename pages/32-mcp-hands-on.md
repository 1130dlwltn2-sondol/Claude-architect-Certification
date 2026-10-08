# 32. 실습: MCP 서버 구축

이론을 손으로 확인하는 시간입니다. Python MCP SDK로 간단한 서버를 만들고, MCP Inspector로 테스트한 뒤 Claude Desktop에 연결합니다. Part 7의 실전 프로젝트도 같은 흐름으로 진행됩니다.

## 준비

Python 3.10 이상과 pip이 필요합니다.

```bash
pip install "mcp[cli]"
```

mcp 패키지의 cli extra를 설치하면 서버 실행과 Inspector 테스트에 필요한 도구가 함께 들어옵니다.

## 서버 코드 작성

날씨 조회 도구와 메모 리소스를 제공하는 서버를 만듭니다. 파일 이름은 weather_server.py로 합니다.

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather-memo")

# 도구: 날씨 조회 (예시 데이터 반환)
@mcp.tool()
def get_weather(city: str) -> str:
    """지정한 도시의 현재 날씨를 조회합니다.
    여행 계획이나 외출 준비를 물을 때 사용하세요.
    도시 이름은 한글 또는 영문으로 입력하세요."""
    sample = {
        "서울": "맑음, 22도",
        "부산": "흐림, 24도",
        "제주": "비, 21도",
    }
    return sample.get(city, f"{city}의 날씨 정보를 찾을 수 없습니다.")

# 리소스: 메모 읽기
@mcp.resource("memo://today")
def today_memo() -> str:
    """오늘의 메모를 제공합니다."""
    return "15시 팀 회의, 17시 배포 리뷰"

if __name__ == "__main__":
    mcp.run()
```

30장에서 배운 도구 설명 원칙이 코드에 녹아 있습니다. 무엇을 하는지, 언제 쓰는지가 docstring에 담겨 있습니다.

## Inspector로 테스트

```bash
mcp dev weather_server.py
```

MCP Inspector가 브라우저에서 열립니다. 여기서 다음을 확인합니다.

1. Tools 탭에서 get_weather가 보이는가
2. city에 "서울"을 넣고 호출하면 "맑음, 22도"가 돌아오는가
3. Resources 탭에서 memo://today를 읽으면 메모가 보이는가

Inspector는 서버 개발의 기본 도구입니다. Claude에 연결하기 전에 여기서 먼저 동작을 확정하세요.

## Claude Desktop에 연결

Claude Desktop의 설정 파일에 서버를 등록합니다.

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json
Windows: %APPDATA%/Claude/claude_desktop_config.json

```json
{
  "mcpServers": {
    "weather-memo": {
      "command": "python",
      "args": ["/절대경로/weather_server.py"]
    }
  }
}
```

Claude Desktop을 재시작하면 서버가 연결됩니다. 대화창에서 "서울 날씨 어때?"라고 물어보면, 모델이 get_weather 도구를 호출하는 것을 볼 수 있습니다.

## Claude Code에 연결

Claude Code에서는 명령어로 추가합니다.

```bash
claude mcp add weather-memo -- python /절대경로/weather_server.py
```

연결 후 /mcp 명령어로 상태를 확인할 수 있습니다.

## 트러블슈팅

서버가 연결되지 않을 때 확인할 것들:

1. args의 경로가 절대경로인가 (상대경로는 동작하지 않는 경우가 많습니다)
2. python이 PATH에 있는가 (가상환경이라면 해당 python의 절대경로를 씁니다)
3. Inspector에서는 되는데 Claude에서 안 되면 설정 파일의 JSON 문법을 확인합니다
4. 서버 로그: stdio 서버의 로그는 stderr로 내보내야 합니다. stdout에 찍으면 프로토콜이 깨집니다

4번은 시험에도 나올 수 있는 실무 포인트입니다. MCP의 stdio 전송에서 stdout은 프로토콜 메시지 전용입니다.

## 실습 과제

1. get_weather에 습도 정보를 추가해 보세요
2. 메모를 추가하는 add_memo 도구를 만들어 보세요 (메모는 파일에 저장)
3. add_memo 실행 전에 사용자 확인을 받으려면 어떻게 해야 할까요? (힌트: 31장의 Elicitation)

3번은 정답이 하나가 아닙니다. Elicitation을 쓰는 방법과, 클라이언트 측에서 승인 프롬프트를 거는 방법을 비교해 보세요.

확인 문제

1. FastMCP의 @mcp.tool() 데코레이터가 하는 일을 설명해 보세요.
2. stdio 서버에서 로그를 stderr로 내보내야 하는 이유를 설명해 보세요.
3. Inspector를 쓰는 이유를 개발 흐름 관점에서 설명해 보세요.
