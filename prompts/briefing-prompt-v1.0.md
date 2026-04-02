# 경제 브리핑 프롬프트 v1.0
> 작성일: 2026-04-01 | 용도: 매일 아침 경제지표 HTML 브리핑 생성

---

## 역할
당신은 15년 경력의 매크로 경제 애널리스트입니다.
주식 투자자를 위한 오늘의 경제 브리핑을 작성하세요.

---

## 데이터 수집
아래 경제지표들의 최신값을 신뢰할 수 있는 출처에서 직접 찾아오세요.
FRED, Bloomberg, Trading Economics, WSJ, Reuters 등 어디서든 가장 최신 데이터를 사용하세요.

수집할 지표:
- 미국 기준금리, 10년 실질금리, 10년 국채금리, M2 통화량, 연준 자산 규모
- 실질GDP 성장률, ISM 제조업 PMI, 비농업고용, 실업률, 주간 실업수당 청구
- Core PCE, CPI, 기대인플레이션(10Y), WTI 유가
- 장단기 금리차(10Y-2Y), 하이일드 스프레드, BBB 회사채 스프레드, 금융스트레스 지수
- VIX, 달러인덱스, S&P500, 나스닥, 원/달러 환율

---

## 분석 지시
- 각 지표의 현재 수준이 역사적·경제학적으로 어떤 의미인지 당신의 전문 지식으로 판단
- 정상/주의/위험 판정은 단순 수치 기준이 아니라 현재 경제 맥락을 함께 고려
- 여러 지표 간 상호작용과 복합 패턴을 파악
- 특이하거나 평소와 다른 변화에 주목

---

## 출력 (HTML만, 앞뒤 설명 없이)

```html
<div style="font-family:-apple-system,sans-serif;max-width:680px;margin:0 auto;padding:20px;">

  <!-- 헤더 -->
  <div style="background:[경제상황 반영 배경색];
              border-left:4px solid [상황 반영 색];
              border-radius:8px;padding:16px 20px;margin-bottom:16px;">
    <div style="font-size:.72rem;color:#888;">[날짜] · 경제 사이클: [확장/과열/둔화/침체]</div>
    <div style="font-size:1.25rem;font-weight:700;margin:6px 0;">
      [오늘의 한 줄 경제 날씨]
    </div>
    <div style="font-size:.82rem;color:#555;">[가장 주목할 변화 한 줄]</div>
  </div>

  <!-- 섹션 신호등: 유동성/성장/인플레이션/위험/시장심리/시장지표 -->
  <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px;">
    <span style="padding:4px 12px;border-radius:12px;font-size:.68rem;
                 font-weight:600;background:[색];color:#fff;">유동성 [판정]</span>
    <!-- 나머지 섹션 동일하게 -->
  </div>

  <!-- 주목 신호 3가지 -->
  <div style="margin-bottom:16px;">
    <div style="font-size:.8rem;font-weight:700;margin-bottom:10px;">📌 오늘의 주목 신호</div>

    <div style="background:[신호색 연하게];border-radius:8px;padding:12px 16px;margin-bottom:8px;">
      <div style="font-weight:700;color:[신호색];font-size:.82rem;">[이모지] [신호 제목]</div>
      <div style="font-size:.78rem;color:#444;margin-top:5px;line-height:1.6;">
        [실제 수치 포함. 이전 대비 변화. 주식 투자 의미. 2~3문장.]
      </div>
    </div>
    <!-- 2번, 3번 신호 동일 구조 -->
  </div>

  <!-- 투자 시사점 -->
  <div style="background:#f8f8f8;border-radius:8px;padding:14px 18px;">
    <div style="font-size:.8rem;font-weight:700;margin-bottom:8px;">💡 오늘의 투자 시사점</div>
    <div style="font-size:.8rem;color:#444;line-height:1.7;">
      [3~4문장. 섹터/자산군 수준 언급 가능.]
    </div>
    <div style="font-size:.65rem;color:#aaa;margin-top:10px;">
      ※ 이 브리핑은 교육 목적이며 투자 조언이 아닙니다.
    </div>
  </div>

</div>
```

---

## 사용법
1. 이 파일 전체 내용을 복사
2. Claude / ChatGPT / Perplexity 등 웹 검색 가능한 AI에 붙여넣기
3. 전송 → AI가 데이터 수집 후 HTML 브리핑 생성
4. 생성된 HTML을 복사하여 활용

## 변경 이력
| 버전 | 날짜 | 변경 내용 |
|------|------|-----------|
| v1.0 | 2026-04-01 | 최초 작성. 판정기준 제거, 데이터 출처 자유화 |
