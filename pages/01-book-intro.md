# 01. 책 소개

## 이 책을 쓴 이유

2026년 3월, Anthropic은 첫 공식 기술 자격증인 Claude Certified Architect – Foundations를 출시했습니다. AWS나 구글 클라우드의 자격증이 클라우드 아키텍트라는 직군을 만들었듯, 이 자격증은 Claude로 실제 시스템을 설계하고 운영하는 역량을 증명하는 기준이 되었습니다. 같은 해 7월에는 Pearson과 손잡고 Associate, Developer, Architect Foundations, Architect Professional의 4종 체계로 확장되었습니다.

문제는 한국어 학습 자료가 거의 없다는 점입니다. 공식 문서는 영어이고, 시험 가이드는 파트너 네트워크 안에서만 볼 수 있습니다. 이 책은 그 간극을 메우기 위해 썼습니다. 초급자가 첫 장부터 따라오면 마지막 장에서는 직접 MCP 서버를 만들고, 모의고사를 풀고, 시험장에 들어갈 준비가 되도록 구성했습니다.

## 대상 독자

- Claude를 써본 적은 있지만 API나 에이전트를 직접 다뤄본 적은 없는 초급자
- 사내에 AI 도입을 검토하거나 파일럿을 운영 중인 개발자
- 솔루션 아키텍트, 기술 컨설턴트, SI/파트너사 실무자
- 자격증 자체보다 에이전트 설계 실력을 체계적으로 쌓고 싶은 사람

선수 지식은 파이썬 기초 문법과 REST API가 무엇인지 아는 정도면 충분합니다. 각 장에서 필요한 개념은 그때그때 설명합니다.

## 책의 구성

Part 1에서는 자격증 제도 전체를 파악합니다. 시험 형식, 5개 도메인의 가중치, 응시 절차, 그리고 8주 학습 플랜을 다룹니다.

Part 2부터 Part 6까지는 시험의 5개 도메인을 순서대로 학습합니다. 가중치가 높은 순서가 아니라, 이해의 순서대로 배열했습니다. 에이전트의 큰 그림을 먼저 잡고(Domain 1), 도구를 설계하고 MCP로 연결하는 법을 배우고(Domain 2), Claude Code로 개발 워크플로우를 자동화하고(Domain 3), 프롬프트를 정교하게 다루고(Domain 4), 마지막으로 컨텍스트와 신뢰성으로 전체를 묶습니다(Domain 5).

Part 7은 이 책이 직접 선정한 실전 프로젝트입니다. MCP 서버를 직접 구축해 Claude Code와 연동하는 사내 지식 어시스턴트를 만듭니다. Domain 2의 내용을 손으로 익히는 과정이기도 합니다.

Part 8은 도메인 가중치를 반영한 모의고사 40문항과 상세 해설입니다. Part 9에서는 시험 당일 전략과 자격 유지, 다음 단계인 Professional 시험을 안내합니다.

## 학습 방법

1. Part 1을 읽고 전체 지도부터 그립니다. 시험이 무엇을 묻는지 알아야 공부가 헛돌지 않습니다.
2. 각 장의 예제 코드는 직접 실행해 봅니다. 눈으로만 읽은 지식은 시험장에서 잘 떠오르지 않습니다.
3. 장 끝의 확인 문제로 이해도를 점검합니다. 틀린 문제는 해당 절을 다시 읽습니다.
4. Part 7 프로젝트는 건너뛰지 마세요. 손으로 만든 경험이 시나리오형 문항의 정답률을 바꿉니다.
5. 마지막 2주는 Part 8 모의고사를 시간을 재고 풉니다. 120분에 60문항, 즉 문항당 2분 페이스를 몸에 익힙니다.

## 표기와 약속

- 코드와 파일 경로는 고정폭 글씨로 표기합니다.
- 실습은 macOS와 Windows, Linux 모두에서 따라할 수 있도록 작성했습니다. 명령어가 OS마다 다르면 각각 표기합니다.
- 시험 관련 수치(응시료, 문항 수, 합격 점수 등)는 기준일 현재 공식 발표 자료를 기준으로 했습니다. 변경 가능성이 있으니 응시 전 공식 가이드를 다시 확인하세요.
- 약어는 처음 나올 때 원어를 함께 적습니다. 예: MCP(Model Context Protocol).

## 참고한 공식 자료

- Anthropic 공식 뉴스: Claude Partner Network, Services Track and Partner Hub, Deloitte 파트너십
- Anthropic Engineering: Building Effective Agents
- Model Context Protocol 공식 문서: Architecture overview
- Anthropic Academy(anthropic.skilljar.com)의 공개 과정
- Pearson VUE의 Claude Certification Program 안내

공식 시험 가이드와 등록은 Anthropic Partner Academy에서 확인할 수 있습니다. 시험 응시에는 Claude Partner Network 회원 자격이 필요합니다.
