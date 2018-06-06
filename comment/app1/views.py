from django.shortcuts import render, HttpResponse

# Create your views here.


def comment_dict(comment_list):

    # def digui(ret, row):
    #     for i in ret:
    #         if i['id'] == row['parent_id']:
    #             row['child'] = []
    #             i['child'].append(row)
    #             return
    #         else:
    #             digui(i['child'], row)

    # def gsh(list1):
    #     i = []
    #     for item in comment_list:
    #         if item['parent_id'] == None:
    #             item['child'] = []
    #             i.append(item)
    #         else:
    #             digui(i, item)
    #     return i
    ret = []
    comment_list_dict = {}
    for row in comment_list:
        row.update({'children': []})
        comment_list_dict[row['id']] = row

    for item in comment_list:

        current_row_parent_id = item['parent_id']
        if not current_row_parent_id:
            ret.append(item)
        else:
            comment_list_dict[current_row_parent_id]['children'].append(item)
    return ret

def index(request):
    
    return render(request, 'index.html')

def comment(request):
    newid = request.GET.get('newid')
    
    #假设根据newid从数据库中获得以下数据
    comment_list = [
        {'id': 1, 'content': '1级评论', 'user': 'w', 'parent_id': None},
        {'id': 2, 'content': '1级评论', 'user': 'w', 'parent_id': None},
        {'id': 3, 'content': '1级评论', 'user': 'w', 'parent_id': None},
        {'id': 4, 'content': '2级评论', 'user': 'l', 'parent_id': 1},
        {'id': 5, 'content': '2级评论', 'user': 'z', 'parent_id': 1},
        {'id': 6, 'content': '3级评论', 'user': 'p', 'parent_id': 4},
        {'id': 7, 'content': '2级评论', 'user': 'w', 'parent_id': 2},
        {'id': 8, 'content': '2级评论', 'user': 'z', 'parent_id': 3},
        {'id': 9, 'content': '3级评论', 'user': 'o', 'parent_id': 8},
        {'id': 10, 'content': '1级评论', 'user': 'u', 'parent_id': None},
    ]
    comment_list = comment_dict(comment_list)

    import json
    return HttpResponse(json.dumps(comment_list))


