import pandas as pd
import os
import sys


def out_csv(file, csv_data, csv_header):
    not_d_pd = pd.DataFrame(csv_data)
    not_d_pd.to_csv(file, header=csv_header, index=False)


if __name__ == '__main__':
    file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
    csv_file = file_path + '/csv/data.csv'
    print("文件路径："+csv_file)

    if not os.path.exists(csv_file):
        print("文件不存在")
        sys.exit(0)
    csv_list = pd.read_csv(csv_file, index_col=False)
    header = csv_list.keys()
    data = csv_list.values
    if data[0] is None:
        print("未找到合适的数据")
    not_d_data = []
    not_d_with_staff_id = []
    with_d = []
    for i in data:
        if i[8] != "D":
            not_d_data.append(i)
            if i[12] == "QDCN1JMYLCL":
                not_d_with_staff_id.append(i)
        else:
            with_d.append(i)

    out_csv(file_path + '/out_csv/not_d.csv', not_d_data, header)
    out_csv(file_path + '/out_csv/not_d_with_staff_id.csv', not_d_with_staff_id, header)
    out_csv(file_path + '/out_csv/with_d.csv', with_d, header)
    print("数据导出完成")
