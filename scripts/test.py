import os
import json

root_dir = 'F:\\KeaPlus-Evaluation\\scripts\\output#2025-04-24-20-34-18\\all_states'
dirs = os.listdir(root_dir)

# 筛选出所有的json文件，并按编号排序
json_files = [f for f in dirs if f.endswith('.json')]
json_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]))

foreground_activities = []

system_activities = 0

# 逐个读取json文件，并提取"foreground_activity"属性
for json_file in json_files:
    file_path = os.path.join(root_dir, json_file)
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        foreground_activity = data.get('foreground_activity')
        if foreground_activity is not None:
            package_name = foreground_activity.split('.', 2)[1]
            print(package_name)
            if package_name != 'ichi2':
                system_activities += 1
            else:
                activity_name = foreground_activity.rsplit('.', 1)[-1]
                foreground_activities.append(activity_name)

# 行程长度编码压缩foreground_activities列表
compressed_activities = []
current_activity = None
count = 0

for activity in foreground_activities:
    if activity == current_activity:
        count += 1
    else:
        if current_activity is not None:
            compressed_activities.append({"count": count, "name": current_activity})
        current_activity = activity
        count = 1

# 添加最后一个活动
if current_activity is not None:
    compressed_activities.append({"count": count, "name": current_activity})


compressed_activities = [activity for activity in compressed_activities if activity['name'] not in ['IntroductionActivity', 'PermissionsActivity']]

print(compressed_activities)
print(f"System activities: {system_activities}")


activity_count = {}
for activity in foreground_activities:
    if activity in activity_count:
        activity_count[activity] += 1
    else:
        activity_count[activity] = 1

print(activity_count)