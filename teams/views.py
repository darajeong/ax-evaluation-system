from django.shortcuts import render


def team_list(request):
    teams = [
        {
            "name": "AI 기반 서비스 기획",
            "member_count": 5,
            "members": "김민수, 이서연, 박지훈 외 2명",
            "status": "확정",
            "created_at": "2026-08-12",
        },
        {
            "name": "AX 아이디어 제안",
            "member_count": 4,
            "members": "이수진, 최민준, 정하은 외 1명",
            "status": "확정",
            "created_at": "2026-08-11",
        },
        {
            "name": "추천 시스템 성능 분석",
            "member_count": 5,
            "members": "박지훈, 김다은, 유현우 외 2명",
            "status": "편성 중",
            "created_at": "2026-08-10",
        },
    ]

    context = {
        "total_teams": 6,
        "total_students": 24,
        "average_members": 4.0,
        "unassigned_students": 0,
        "teams": teams,
    }
    return render(request, "teams/team_list.html", context)