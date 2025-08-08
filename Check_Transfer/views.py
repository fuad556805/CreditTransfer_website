from django.shortcuts import render
from django.db import connection

def check(request):
    source_uni_list = ['EWU', 'NSU', 'BRAC', 'IUB', 'AIUB']
    target_uni_list = ['EWU', 'NSU', 'BRAC', 'IUB', 'AIUB']
    subject_list = ['CSE', 'EEE', 'CIVIL', 'BBA', 'ENG']

    results = []
    total_credit = 0

    if request.method == 'POST':
        source = request.POST.get('source_uni')
        target = request.POST.get('target_uni')
        subject = request.POST.get('subject')

        query = """
        SELECT s.course_code, s.course_name, s.course_credit
        FROM similar_courses s
        INNER JOIN similar_courses t
        ON s.course_code = t.course_code
        WHERE s.university_name = %s AND t.university_name = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [source, target])
            results = cursor.fetchall()
            total_credit = sum([row[2] for row in results])  # sum of course_credit

    context = {
        'source_uni_list': source_uni_list,
        'target_uni_list': target_uni_list,
        'subject_list': subject_list,
        'results': results,
        'total_credit': total_credit,
    }
    return render(request, 'Check_Transfer/check.html', context)
