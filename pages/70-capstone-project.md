# 70. 실전 프로젝트: MCP 지식 어시스턴트 만들기

이 장은 이 책이 직접 선정한 실전 프로젝트입니다. 지금까지 배운 것을 하나로 묶어, MCP 서버와 Claude Code를 연동한 사내 지식 어시스턴트를 만듭니다. Domain 2의 실습이자, 시험의 시나리오형 문항을 몸으로 익히는 과정입니다.

왜 이 주제인가. MCP는 현재 가장 주목받는 AI 연동 표준입니다. 한 번 만들면 Claude Code, Claude Desktop 등 여러 호스트에서 쓸 수 있고, 사내 문서 검색이라는 문제는 거의 모든 조직에 있습니다. 배운 것을 실제 업무에 바로 연결할 수 있는 주제입니다.

## 프로젝트 개요

만들 것: "사내 기술 문서 검색 MCP 서버 + Claude Code 연동"

사용 장면: 개발자가 "배포 절차가 어떻게 되지?"라고 물으면, Claude Code가 MCP 서버를 통해 사내 문서를 검색하고 근거와 함께 답합니다.

구성 요소:

- MCP 서버 (Python): 문서 검색 도구, 문서 읽기 리소스 제공
- 문서 저장소: 마크다운 파일들의 폴더
- Claude Code: MCP 서버에 연결된 코딩 어시스턴트

## 1단계: 문서 준비

docs/ 폴더를 만들고 예시 문서 3개를 넣습니다.

docs/deploy.md:
```markdown
# 배포 절차
1. main 브랜치에 머지한다
2. CI가 통과하는지 확인한다
3. 배포 버튼을 누른다
4. 헬스체크가 정상인지 5분간 관찰한다
```

docs/onboarding.md, docs/troubleshooting.md도 비슷한 형식으로 만듭니다. 실제 사내 문서가 있다면 그걸 써도 됩니다.

## 2단계: MCP 서버 구현

32장의 서버를 확장합니다. 파일 이름은 knowledge_server.py입니다.

```python
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("knowledge-base")
DOCS_DIR = os.path.join(os.path.dirname(__file__), "docs")

def _list_docs():
    return [f for f in os.listdir(DOCS_DIR) if f.endswith(".md")]

@mcp.tool()
def search_docs(keyword: str) -> str:
    """사내 기술 문서에서 키워드가 포함된 문서를 검색합니다.
    절차, 정책, 트러블슈팅을 물을 때 사용하세요.
    keyword는 1~3개의 핵심 단어로 입력하세요."""
    hits = []
    for name in _list_docs():
        path = os.path.join(DOCS_DIR, name)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        if keyword in content:
            hits.append(f"## {name}\n{content[:500]}")
    if not hits:
        return f"'{keyword}'와 관련된 문서를 찾지 못했습니다."
    return "\n\n".join(hits)

@mcp.tool()
def read_doc(filename: str) -> str:
    """지정한 문서를 전체 읽습니다.
    search_docs로 찾은 문서의 전체 내용이 필요할 때 사용하세요.
    filename은 search_docs 결과에 나온 파일 이름 그대로 입력하세요."""
    path = os.path.join(DOCS_DIR, filename)
    if not os.path.exists(path):
        return f"'{filename}' 문서를 찾을 수 없습니다."
    with open(path, encoding="utf-8") as f:
        return f.read()

@mcp.resource("docs://list")
def docs_list() -> str:
    """보유 문서 목록을 제공합니다."""
    return "\n".join(_list_docs())

if __name__ == "__main__":
    mcp.run()
```

설계 포인트:

- search_docs와 read_doc의 역할 분리: 검색은 요약, 읽기는 전문. 30장의 "하나의 명확한 목적" 원칙입니다
- 도구 설명에 언제 쓰는지 명시
- 파일이 없을 때의 에러 메시지 포함

## 3단계: 테스트

```bash
mcp dev knowledge_server.py
```

Inspector에서 확인:

1. search_docs에 "배포"를 넣어 deploy.md가 나오는가
2. read_doc에 "deploy.md"를 넣어 전문이 나오는가
3. 없는 키워드/파일에 대한 에러 메시지가 적절한가

## 4단계: Claude Code에 연결

```bash
claude mcp add knowledge-base -- python /절대경로/knowledge_server.py
```

연결 후 질문해 봅니다.

- "배포 절차 알려줘"
- "온보딩할 때 뭘 해야 돼?"

Claude Code가 도구를 호출해 문서 근거로 답하는지 확인합니다. 답에 문서 내용이 반영되지 않으면, 도구 설명이나 검색 로직을 점검합니다.

## 5단계: 개선하기

기본 동작이 되면 다음을 시도합니다.

1. 관련도 순 정렬: 키워드 출현 횟수로 정렬해 보세요
2. 청킹: 문서가 길어지면 섹션 단위로 나눠 검색하세요 (61장의 RAG)
3. 캐싱 고려: 문서가 자주 바뀌지 않는다면 읽기 결과를 메모리에 둡니다
4. 권한: 민감한 문서는 별도 폴더로 분리하고 서버에서 제외합니다

## 6단계: 회고

프로젝트가 끝나면 다음 질문에 답해봅니다.

1. 이 서버를 다른 팀에 소개한다면 어떻게 설명하겠습니까?
2. 문서가 1,000개로 늘어나면 무엇이 바뀌어야 합니까? (힌트: 61장)
3. 잘못된 문서가 있을 때 시스템은 어떻게 동작합니까? (힌트: 22장, 62장)
4. 이 프로젝트에서 시험에 나올 만한 개념 5가지를 뽑아보세요

4번의 답 예시: MCP 프리미티브, 도구 설계 원칙, stdio 전송, 컨텍스트 선택, 신뢰성(에러 처리).

## 확장 아이디어

- 웹 검색 도구 추가: 사내 문서에 없으면 외부 검색으로 폴백 (62장의 폴백)
- 슬랙 연동: 질문을 슬랙에서 받아 답하는 봇 (MCP 서버는 그대로 재사용)
- 평가: 자주 묻는 질문 20개를 정해놓고 정기적으로 품질 측정 (22장의 시나리오 평가)

이 프로젝트의 코드는 저장소의 examples/ 폴더에 정리해 두면, 시험 복습용 포트폴리오가 됩니다.
