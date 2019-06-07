import operator

# input : file의 이름, 단위 시간, 출력할 결과의 개수
def extraction_highlight(file_path, interval, number_of_results):
    file = open(file_path, 'r', encoding='UTF8')
    lines = file.readlines()
    file.close()

    start_time = 0
    end_time = interval - 1
    count = 0
    count_dict = dict()
    
    for line in lines:
        h, m, s = parsing_hms(line)
        sec = hms_to_s(h, m, s)

        if sec <= end_time:
            count = count + 1
        else:
            count_dict[start_time] = count
            count = 0
            start_time += interval
            end_time += interval
    if count != 0:
        count_dict[start_time] = count

    rank = sorted(count_dict.items(), key = operator.itemgetter(1), reverse = True)

    result = list()

    for i in range(number_of_results):
        s_h, s_m, s_s = s_to_hms(rank[i][0])
        e_h, e_m, e_s = s_to_hms(rank[i][0] + interval - 1)

        result.append(((s_h, s_m, s_s), (e_h, e_m, e_s)))

    return result

def hms_to_s(h, m, s):
    return h * 3600 + m * 60 + s

def s_to_hms(s):
    h = int(s / 3600)
    s = s % 3600
    m = int(s / 60)
    s = s % 60

    return (h, m, s)

# hour가 1자리 or 2자리
def parsing_hms(str):
    # hour가 1 자리
    if str[2] == ':':
        h = str[1]
        m = str[3:5]
        s = str[6:8]
    else:
        h = str[1:3]
        m = str[4:6]
        s = str[7:9]

    return (int(h), int(m), int(s))

# 사용 예시입니다.
if __name__ == "__main__":
    file_path = "C:/python/nlp/overwatch.txt"
    interval = 30
    number_of_results = 10

    result = extraction_highlight(file_path, interval, number_of_results)
    print(result)

