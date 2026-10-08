#!/usr/bin/env python3
"""Claude Architect Certification 책용 이미지 생성 스크립트 (PIL 기반)."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")

BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
SERIFB = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"

BG = (13, 19, 38)
PANEL = (24, 33, 62)
PANEL2 = (30, 42, 76)
CORAL = (224, 120, 86)
TEAL = (78, 205, 196)
BLUE = (96, 150, 255)
WHITE = (245, 247, 250)
MUTED = (154, 167, 199)
LINE = (70, 88, 140)


def font(path, size):
    return ImageFont.truetype(path, size, index=1)


def text_center(d, cx, y, s, f, fill):
    bb = d.textbbox((0, 0), s, font=f)
    w = bb[2] - bb[0]
    d.text((cx - w / 2 - bb[0], y), s, font=f, fill=fill)


def rrect(d, box, radius, fill, outline=None, width=1):
    d.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(d, x1, y1, x2, y2, fill=CORAL, width=4):
    d.line([x1, y1, x2, y2], fill=fill, width=width)
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    sz = 14
    for da in (2.6, -2.6):
        d.line([x2, y2, x2 + sz * math.cos(ang + da), y2 + sz * math.sin(ang + da)],
               fill=fill, width=width)


# ---------------------------------------------------------------- 표지 1000x1300
def make_cover():
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # 배경 그라데이션
    for y in range(H):
        t = y / H
        r = int(13 + (30 - 13) * t)
        g = int(19 + (44 - 19) * t)
        b = int(38 + (82 - 38) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    # 장식 원
    d.ellipse([-180, -180, 320, 320], outline=(224, 120, 86, 90), width=3)
    d.ellipse([-120, -120, 260, 260], outline=(78, 205, 196, 70), width=2)
    d.ellipse([760, 980, 1180, 1400], outline=(96, 150, 255, 80), width=3)
    d.ellipse([820, 1040, 1120, 1340], outline=(224, 120, 86, 60), width=2)
    # 대각선 라인 장식
    for i in range(6):
        x = 700 + i * 45
        d.line([(x, 0), (x + 220, 420)], fill=(255, 255, 255, 14), width=2)

    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    # 상단 뱃지
    text_center(d, W / 2, 66, "W I K I D O C S   T E C H   B O O K", fr(26), CORAL)
    d.line([(120, 128), (880, 128)], fill=LINE, width=2)

    # 메인 타이틀
    text_center(d, W / 2, 190, "Claude Certified", fb(92), WHITE)
    text_center(d, W / 2, 305, "Architect", fb(112), CORAL)

    # 한글 부제
    text_center(d, W / 2, 478, "클로드 인증 아키텍트", fb(58), WHITE)
    text_center(d, W / 2, 556, "자격증 준비", fb(58), WHITE)

    # 설명 문구
    rrect(d, [160, 660, 840, 728], 34, PANEL, outline=LINE, width=2)
    text_center(d, W / 2, 676, "초급자부터 시작하는 실전 대비서", fb(32), WHITE)

    # 도메인 목록
    domains = [
        "Agentic Architecture and Orchestration",
        "Tool Design and MCP Integration",
        "Claude Code Configuration and Workflows",
        "Prompt Engineering and Structured Output",
        "Context Management and Reliability",
    ]
    y = 768
    text_center(d, W / 2, y, "5 Exam Domains", fr(26), MUTED)
    y += 44
    for i, dom in enumerate(domains):
        rrect(d, [170, y, 830, y + 46], 23, (20, 28, 54), outline=(60, 76, 120), width=1)
        d.ellipse([194, y + 11, 228, y + 45], fill=CORAL)
        fnum = fb(26)
        num = str(i + 1)
        bb = d.textbbox((0, 0), num, font=fnum)
        d.text((211 - (bb[2] - bb[0]) / 2 - bb[0], y + 13), num, font=fnum, fill=(255, 255, 255))
        d.text((244, y + 15), dom, font=fr(22), fill=WHITE)
        y += 56

    # 하단 정보
    d.line([(120, 1130), (880, 1130)], fill=LINE, width=2)
    text_center(d, W / 2, 1158, "저자  이준수", fr(30), MUTED)
    text_center(d, W / 2, 1202, "기준일  2026-04-05", fr(26), MUTED)

    img.save(os.path.join(ASSETS, "cover.png"))
    print("cover.png saved")


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    make_cover()


# ------------------------------------------------- 자격증 로드맵 1400x520
def make_roadmap():
    W, H = 1400, 520
    img = Image.new("RGB", (W, H), (250, 251, 253))
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 28, "Claude Certification Program (2026)", fb(40), (30, 41, 59))
    text_center(d, W / 2, 84, "Pearson VUE proctored  |  Credly digital badge  |  valid 12 months",
                fr(26), (100, 116, 139))

    cards = [
        ("Associate", "Foundations", "고객 상담과\n도입 자문", TEAL),
        ("Developer", "Foundations", "API·Claude Code·\nMCP로 빌드", BLUE),
        ("Architect", "Foundations", "솔루션 end-to-end\n설계", CORAL),
        ("Architect", "Professional", "엔터프라이즈급\n아키텍처 심화", (139, 92, 246)),
    ]
    x0, cw, gap = 60, 280, 40
    y0 = 150
    for i, (t1, t2, desc, color) in enumerate(cards):
        x = x0 + i * (cw + gap)
        rrect(d, [x, y0, x + cw, y0 + 300], 24, (255, 255, 255),
              outline=(203, 213, 225), width=2)
        d.rectangle([x, y0, x + cw, y0 + 14], fill=color)
        text_center(d, x + cw / 2, y0 + 40, t1, fb(36), (30, 41, 59))
        text_center(d, x + cw / 2, y0 + 88, t2, fr(28), (100, 116, 139))
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + cw / 2, y0 + 150 + j * 44, line, fr(28), (71, 85, 105))
        if i < 3:
            ax = x + cw
            arrow(d, ax + 4, y0 + 150, ax + gap - 4, y0 + 150, fill=(148, 163, 184), width=5)

    text_center(d, W / 2, y0 + 330, "이 책의 범위: Architect Foundations (CCA-F) 전 도메인 + Professional 맛보기",
                fr(26), (100, 116, 139))
    img.save(os.path.join(ASSETS, "fig-cert-roadmap.png"))
    print("fig-cert-roadmap.png saved")


# ------------------------------------------------- 도메인 가중치 1200x640
def make_domains():
    W, H = 1200, 640
    img = Image.new("RGB", (W, H), (250, 251, 253))
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 26, "CCA-F Exam Domains and Weights", fb(40), (30, 41, 59))
    text_center(d, W / 2, 80, "60 questions  |  120 minutes  |  pass 720 / 1000",
                fr(26), (100, 116, 139))

    domains = [
        ("D1", "Agentic Architecture and Orchestration", "에이전트 아키텍처와 오케스트레이션", 27, CORAL),
        ("D3", "Claude Code Configuration and Workflows", "Claude Code 설정과 워크플로우", 20, BLUE),
        ("D4", "Prompt Engineering and Structured Output", "프롬프트 엔지니어링과 구조화 출력", 20, TEAL),
        ("D2", "Tool Design and MCP Integration", "도구 설계와 MCP 통합", 18, (139, 92, 246)),
        ("D5", "Context Management and Reliability", "컨텍스트 관리와 신뢰성", 15, (245, 158, 11)),
    ]
    y = 140
    maxw = 620
    for code, en, ko, w, color in domains:
        text_center(d, 90, y + 8, code, fb(32), (30, 41, 59))
        d.text((150, y), en, font=fr(26), fill=(30, 41, 59))
        d.text((150, y + 36), ko, font=fr(24), fill=(100, 116, 139))
        bw = int(maxw * w / 27)
        rrect(d, [470, y + 6, 470 + bw, y + 52], 12, color)
        d.text((482 + bw, y + 12), f"{w}%", font=fb(30), fill=(30, 41, 59))
        y += 96

    text_center(d, W / 2, H - 46, "가중치가 높은 도메인부터 학습 시간을 배분하세요",
                fr(24), (100, 116, 139))
    img.save(os.path.join(ASSETS, "fig-exam-domains.png"))
    print("fig-exam-domains.png saved")


# ------------------------------------------------- 에이전트 패턴 5종 1500x980
def make_agent_patterns():
    W, H = 1500, 980
    img = Image.new("RGB", (W, H), (250, 251, 253))
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "Agentic Systems: 5 Workflow Patterns + Agents", fb(40), (30, 41, 59))
    text_center(d, W / 2, 76, "Anthropic Building Effective Agents의 핵심 패턴",
                fr(26), (100, 116, 139))

    def box(x, y, w, h, label, fill=(255, 255, 255), tc=(30, 41, 59)):
        rrect(d, [x, y, x + w, y + h], 16, fill, outline=(203, 213, 225), width=2)
        text_center(d, x + w / 2, y + h / 2 - 18, label, fr(24), tc)

    panels = [
        ("1. Prompt Chaining", "프롬프트 체이닝", "순차 단계 분해", CORAL),
        ("2. Routing", "라우팅", "입력 분류 후 분기", BLUE),
        ("3. Parallelization", "병렬화", "독립 작업 동시 수행", TEAL),
        ("4. Orchestrator-Workers", "오케스트레이터-워커", "동적 분해와 위임", (139, 92, 246)),
        ("5. Evaluator-Optimizer", "평가자-최적화", "반복 평가와 개선", (245, 158, 11)),
    ]
    px, py, pw, ph, gapx, gapy = 60, 150, 430, 330, 45, 40
    for i, (en, ko, desc, color) in enumerate(panels):
        cx, cy = px + (i % 3) * (pw + gapx), py + (i // 3) * (ph + gapy)
        rrect(d, [cx, cy, cx + pw, cy + ph], 20, (255, 255, 255),
              outline=(203, 213, 225), width=2)
        d.rectangle([cx, cy, cx + pw, cy + 10], fill=color)
        text_center(d, cx + pw / 2, cy + 30, en, fb(30), (30, 41, 59))
        text_center(d, cx + pw / 2, cy + 70, f"{ko} - {desc}", fr(24), (100, 116, 139))

        ix, iy = cx + 40, cy + 130
        if i == 0:  # chaining: A -> B -> C
            for j in range(3):
                box(ix + j * 130, iy, 110, 70, f"단계 {j + 1}")
                if j < 2:
                    arrow(d, ix + j * 130 + 112, iy + 35, ix + j * 130 + 128, iy + 35,
                          fill=(148, 163, 184), width=4)
        elif i == 1:  # routing: input -> classifier -> 3 branches
            box(ix + 120, iy - 10, 110, 60, "입력")
            arrow(d, ix + 230, iy + 20, ix + 250, iy + 20, fill=(148, 163, 184), width=4)
            box(ix + 250, iy - 10, 90, 60, "분류")
            for j in range(3):
                by = iy + 70 + j * 0
                box(ix + 40 + j * 110, iy + 80, 100, 55, f"전문가 {j + 1}")
                arrow(d, ix + 295, iy + 50, ix + 90 + j * 110, iy + 80,
                      fill=(148, 163, 184), width=3)
        elif i == 2:  # parallel: 1 -> 3 -> aggregate
            box(ix + 15, iy + 45, 90, 60, "입력")
            for j in range(3):
                box(ix + 140, iy - 20 + j * 75, 110, 60, f"작업 {j + 1}")
                arrow(d, ix + 105, iy + 75, ix + 140, iy + 10 + j * 75, fill=(148, 163, 184), width=3)
                arrow(d, ix + 250, iy + 10 + j * 75, ix + 280, iy + 75, fill=(148, 163, 184), width=3)
            box(ix + 280, iy + 45, 90, 60, "집계")
        elif i == 3:  # orchestrator-workers
            box(ix + 105, iy - 15, 180, 60, "오케스트레이터", fill=(237, 233, 254))
            for j in range(3):
                box(ix + 20 + j * 120, iy + 90, 110, 60, f"워커 {j + 1}")
                arrow(d, ix + 195, iy + 45, ix + 75 + j * 120, iy + 90, fill=(148, 163, 184), width=3)
                arrow(d, ix + 75 + j * 120, iy + 120, ix + 195, iy + 45, fill=(148, 163, 184), width=2)
        else:  # evaluator-optimizer loop
            box(ix + 30, iy + 30, 130, 70, "생성기")
            box(ix + 230, iy + 30, 130, 70, "평가자")
            arrow(d, ix + 160, iy + 50, ix + 230, iy + 50, fill=(148, 163, 184), width=4)
            arrow(d, ix + 230, iy + 100, ix + 160, iy + 100, fill=(148, 163, 184), width=4)
            d.text((ix + 165, iy + 108), "피드백", font=fr(22), fill=(100, 116, 139))

    # Agents 패널 (하단 전체)
    ax, ay, aw, ah = px, py + 2 * (ph + gapy), W - 2 * px, 150
    rrect(d, [ax, ay, ax + aw, ay + ah], 20, (30, 41, 59))
    text_center(d, ax + aw / 2, ay + 22, "Agents: LLM이 도구 사용을 스스로 지휘하는 자율 루프", fb(30), (255, 255, 255))
    text_center(d, ax + aw / 2, ay + 66,
                "사용자 지시 -> 계획 -> 도구 호출 -> 환경 피드백 -> 반복 (정지 조건: 완료 또는 최대 반복 횟수)",
                fr(25), (203, 213, 225))
    text_center(d, ax + aw / 2, ay + 104, "원칙: 단순하게, 투명하게, 도구 문서화를 철저히",
                fr(25), CORAL)

    img.save(os.path.join(ASSETS, "fig-agent-patterns.png"))
    print("fig-agent-patterns.png saved")


# ------------------------------------------------- MCP 아키텍처 1400x760
def make_mcp_arch():
    W, H = 1400, 760
    img = Image.new("RGB", (W, H), (250, 251, 253))
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "Model Context Protocol (MCP) Architecture", fb(40), (30, 41, 59))
    text_center(d, W / 2, 76, "Host - Client - Server 구조  |  JSON-RPC 2.0  |  Tools / Resources / Prompts",
                fr(26), (100, 116, 139))

    # Host
    rrect(d, [80, 150, 420, 640], 24, (30, 41, 59))
    text_center(d, 250, 180, "MCP Host", fb(34), (255, 255, 255))
    text_center(d, 250, 228, "AI 애플리케이션", fr(26), (203, 213, 225))
    for j, app in enumerate(["Claude Code", "Claude Desktop", "VS Code"]):
        rrect(d, [120, 300 + j * 100, 380, 368 + j * 100], 16, (51, 65, 92))
        text_center(d, 250, 318 + j * 100, app, fr(28), (255, 255, 255))

    # Clients
    rrect(d, [560, 150, 840, 640], 24, (255, 255, 255), outline=BLUE, width=3)
    text_center(d, 700, 180, "MCP Client", fb(34), (30, 41, 59))
    text_center(d, 700, 228, "서버별 1:1 연결 유지", fr(26), (100, 116, 139))
    for j in range(3):
        rrect(d, [610, 300 + j * 100, 790, 368 + j * 100], 16, (219, 234, 254))
        text_center(d, 700, 318 + j * 100, f"Client {j + 1}", fr(28), (30, 41, 59))
    arrow(d, 430, 395, 550, 395, fill=BLUE, width=5)

    # Servers
    rrect(d, [980, 150, 1320, 640], 24, (255, 255, 255), outline=CORAL, width=3)
    text_center(d, 1150, 180, "MCP Server", fb(34), (30, 41, 59))
    text_center(d, 1150, 228, "컨텍스트 제공 프로그램", fr(26), (100, 116, 139))
    prims = [("Tools", "실행 함수"), ("Resources", "데이터 소스"), ("Prompts", "템플릿")]
    for j, (en, ko) in enumerate(prims):
        rrect(d, [1020, 300 + j * 100, 1280, 368 + j * 100], 16, (255, 237, 230))
        text_center(d, 1150, 312 + j * 100, en, fb(28), (30, 41, 59))
        text_center(d, 1150, 344 + j * 100, ko, fr(22), (100, 116, 139))
    arrow(d, 850, 395, 970, 395, fill=CORAL, width=5)

    # Transport
    text_center(d, W / 2, 680, "Transport: Stdio (로컬)  |  Streamable HTTP (원격, OAuth 권장)",
                fr(26), (100, 116, 139))
    img.save(os.path.join(ASSETS, "fig-mcp-arch.png"))
    print("fig-mcp-arch.png saved")


# ------------------------------------------------- 컨텍스트 파이프라인 1400x560
def make_context_pipeline():
    W, H = 1400, 560
    img = Image.new("RGB", (W, H), (250, 251, 253))
    d = ImageDraw.Draw(img)
    fb = lambda s: font(BOLD, s)
    fr = lambda s: font(REG, s)

    text_center(d, W / 2, 24, "Context Engineering Pipeline", fb(40), (30, 41, 59))
    text_center(d, W / 2, 76, "토큰 비용은 줄이고, 모델에게 꼭 필요한 정보만 전달한다",
                fr(26), (100, 116, 139))

    steps = [
        ("수집", "원본 데이터\n문서·DB·API", (148, 163, 184)),
        ("선택", "검색·랭킹\nRAG · 관련도 필터", BLUE),
        ("압축", "요약·청킹\n불필요 토큰 제거", TEAL),
        ("캐싱", "프롬프트 캐싱\n반복 비용 절감", (139, 92, 246)),
        ("주입", "프롬프트 구성\n시스템+컨텍스트", CORAL),
    ]
    x0, bw, gap = 60, 220, 40
    y0 = 170
    for i, (t, desc, color) in enumerate(steps):
        x = x0 + i * (bw + gap)
        # 깔때기 느낌: 아래로 갈수록 좁아지는 박스 대신 동일 박스 + 토큰 바
        rrect(d, [x, y0, x + bw, y0 + 200], 20, (255, 255, 255),
              outline=(203, 213, 225), width=2)
        d.rectangle([x, y0, x + bw, y0 + 12], fill=color)
        text_center(d, x + bw / 2, y0 + 34, t, fb(32), (30, 41, 59))
        for j, line in enumerate(desc.split("\n")):
            text_center(d, x + bw / 2, y0 + 84 + j * 40, line, fr(24), (71, 85, 105))
        # 토큰 바 (점점 짧아짐)
        tw = int(160 * (1 - i * 0.18))
        d.rectangle([x + 30, y0 + 168, x + 30 + tw, y0 + 182], fill=color)
        if i < 4:
            arrow(d, x + bw + 6, y0 + 100, x + bw + gap - 6, y0 + 100,
                  fill=(148, 163, 184), width=5)

    text_center(d, W / 2, 440, "같은 답변 품질, 더 적은 토큰: 컨텍스트 관리의 핵심 지표",
                fr(26), (100, 116, 139))
    img.save(os.path.join(ASSETS, "fig-context-pipeline.png"))
    print("fig-context-pipeline.png saved")


if __name__ == "__main__":
    import sys
    os.makedirs(ASSETS, exist_ok=True)
    make_cover()
    make_roadmap()
    make_domains()
    make_agent_patterns()
    make_mcp_arch()
    make_context_pipeline()
