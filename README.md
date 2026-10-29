# WARP Lab — Wireless AI and Radio Perception

Allan Lab의 Jekyll/Bootstrap 구성을 바탕으로 만든 WARP Lab 홈페이지 작업본입니다.
저장소는 `proferickim/WARP-LAB`이며, GitHub Pages용 주소 설정은
`https://proferickim.github.io/WARP-LAB/`입니다. 이 주소는 Pages를 활성화한 뒤 사용할 수 있습니다.
본문은 흰색, 주요 제목과 News 영역은 짙은 파랑, 링크와 강조는 초록으로 구성했습니다.

## 구성

- Home: 연구실 소개, 연구 분야, 주요 논문, News
- People: Yonghwi Kim 교수 소개와 CV
- Research: Wireless AI, Radio Perception, Wireless Platforms
- Publications: 기존 홈페이지의 논문 8편과 개별 논문 페이지
- Join Us: 문의 이메일 및 교수실·연구실 위치

## 수정할 파일

| 내용 | 파일 |
| --- | --- |
| 연구실 이름·이메일·위치·주소 | `_config.yml` |
| 메뉴 | `_data/navigation.yml` |
| News | `_data/news.yml` |
| 연구 분야 | `_data/research.yml` |
| 논문 | `_publications/*.md` |
| 소개와 각 페이지 | `_pages/` |
| 공통 레이아웃 | `_layouts/`, `_includes/` |
| 배경색·서체·간격 | `css/main.scss` |

## 서체와 한국어

영문은 Gill Sans, 한글은 SUIT를 사용합니다. Gill Sans가 없는 환경에서는 Calibri, SUIT 순으로 대체됩니다. SUIT 가변 웹폰트는 저장소의 `fonts/`에 포함되어 외부 폰트 서비스 없이 표시됩니다. 상용 Gill Sans 파일은 포함하지 않았습니다.

- 영문 본문·메뉴·제목: Light, 굵기 300
- 한글 소개 본문: 굵기 350, 넉넉한 줄 간격
- 작은 날짜 표기와 위치 안내: 굵기 400
- 메뉴·논문 제목·상세 연구 내용은 영어, 메인 소개·연구 요약·문의 안내·위치는 한국어를 함께 사용합니다.

한국어 문단은 `<p class="ko-copy" lang="ko">내용</p>`, 짧은 보조 설명은 `<p class="ko-caption" lang="ko">내용</p>` 형식으로 작성합니다. 연구 분야의 한글 요약은 `_data/research.yml`의 `short_ko`를 수정합니다. 서체와 굵기는 `css/main.scss`에서 조정할 수 있습니다.

## 로컬 실행

Ruby와 Bundler가 설치된 환경에서:

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1 --port 4177
```

`http://127.0.0.1:4177/WARP-LAB/`에서 확인합니다.

정적 파일 생성:

```sh
JEKYLL_ENV=production bundle exec jekyll build
python3 scripts/check_site.py
```

GitHub Pages와 호환되는 Jekyll 3.10 및 지원 플러그인만 사용합니다. Pages를 활성화할 때 배포 원본을 `main` 브랜치의 루트(`/`)로 지정합니다. 저장소의 공개 여부는 변경하지 않습니다.

## 미리보기 내보내기

```sh
python3 scripts/export_preview.py /absolute/path/to/preview-directory
```

생성된 `index.html`을 열면 서버 없이 메뉴와 논문 페이지를 확인할 수 있습니다. 내보낸 파일은 검토용이며, 실제 GitHub Pages에는 이 저장소의 Jekyll 소스를 사용합니다.

## 내용과 이관 기록

- 현재 공개 홈페이지의 소개, 경력, 논문 8편, 프로필 사진을 이관했습니다.
- 기존 `/publication/...` 주소 8개와 `/cv/`를 유지했습니다.
- `/about/`, `/team/`, `/vacancies/`, `/contact/`, `/allnews.html`은 관련 새 페이지로 연결됩니다.
- 템플릿의 예제 논문 본문, 예제 PDF, 블로그·강의 예제 데이터는 새 사이트에서 제거했습니다. 원본은 Git 이력과 별도 백업 ZIP에 남아 있습니다.
- 교수실 2공학관 411호, 연구실 2공학관 303호를 반영했습니다.
- News는 기존 소개와 논문 메타데이터를 바탕으로 구성했습니다. 임용의 정확한 월·일은 제공되지 않아 연도만 표기했습니다.
- 논문 날짜 및 Early Access 상태는 기존 홈페이지의 정보를 유지했습니다. `iotj25.md`는 기존 날짜(2025)와 원래 인용문의 연도(2026)가 달라 공개 반영 전 서지 정보 확인을 권합니다. 이 초안은 두 값을 임의로 통일하지 않았습니다.
- 연구 분야 도식은 개념 설명용이며 실험 사진이나 측정 결과가 아닙니다.

원형: https://github.com/mpa139/allanlab

