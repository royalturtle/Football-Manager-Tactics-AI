ConstantTactics = {
            "type": 5,  # 1 ~ 7 : 극단적 수비, 수비, 역습, 일반, 지배, 공격, 극단적 공격
            "onball": {
                "offensewidth": 1,  # 1 ~ 5
                "tospace": True,
                "todefense": True,  # 수비 진영 침착
                "towhere": 4,  # 1 ~ 5  { Nothing / 중앙 / 왼쪽 / 오른쪽/ 왼 + 오 }
                "leftgo": 2,  # 1 ~ 3  { Nothing / 오버래핑 / 언더래핑}
                "rightgo": 2,  # 1 ~ 3  { Nothing / 오버래핑 / 언더래핑 }
                "passway": 5,  # 1 ~ 5  패스 방식
                "tempo": 5,  # 1 ~ 5  템포
                "timewaste": 2,  # 1 ~ 3  시간 보내기
                "crosstype": 2,  # 1 ~ 4  크로스 방식 { 혼합/ 높은 / 채찍 / 낮은 }
                "crosshow": 3,  # 1 ~ 5 { Nothing / 침착하게 골 찬스를 / 빠르게 크로스 / 아끼지 말라/ 아끼지 + 빠르게}
                "setplay": True,  #
                "dribble": 2,  # 1 ~ 3  { Nothing / 드리블 적게 / 수비진을 뚫어라 }
                "creativity": 2  # 1 ~ 3 { Nothing / 자유롭게 / 전술대로 }
            },
            "change": {
                "ballno": 2,  # 1 ~ 3  { 1: Nothing, 2 : 역 압박, 3: 재정비 }
                "ballyes": 3,  # 1 ~ 3  , { 1: Nothing, 2 : 역습, 3: 진형 유지 }
                "keepercatch": 1,  # 1 ~ 3  { 1: Nothing, 2 : 빠르게, 3 : 천천히 }
                "keepergive": 23  # 1 ~ 26
                # Nothing
                # 상대 수비진 넘겨 배급 (Nothing / 멀리 차라)
                # 타겟맨에게 배급 (Nothing / 멀리 차라)
                # 측면으로 배급 ( Nothing / 멀리 던져라 / 발로 짧은 패스 / 멀리 차라)
                # 플레이메이커 배급 ( Nothing / 굴려서 배급 / 멀리 던져라 / 발로 짧은 패스 / 멀리 차라)
                # 풀백에게 배급 (Nothing / 굴려서 배급 / 멀리 던져라 / 발로 짧은 패스)
                # 센터백에게 배급 (Nothing / 굴려서 배급 / 멀리 던져라 / 발로 짧은 패스) ~ 22
                # 풀백 + 센터백에게 배급 (Nothing / 굴려서 배급 / 멀리 던져라 / 발로 짧은 패스) ~ 26
            },
            "offball": {
                "offsidetrap": True,
                "offenseline": 2,  # 1 ~ 5
                "defenseline": 1,  # 1 ~ 5
                "defensewidth": 1,  # 1 ~ 3
                "mark": True,
                "pressure": 4,  # 1 ~ 5
                "longpassinduce": True,
                "tackle": 2  # 1 : Nothing, 2 : 서서, 3 : 아끼지 말아라
            }
        }