#!/bin/bash

# 配置参数
INTERVAL_MINUTES=70         # 间隔时间（分钟）
MAX_RUNS=5                  # 最大运行次数

# 执行循环
run_count=0
while [ $run_count -lt $MAX_RUNS ]
do
    # 增加计数器
    ((run_count++))
    
    echo "【执行开始】第 $run_count 次运行 (时间: $(date))"
    
    bash -x ./run_Kea.sh "../AmazeFileManager/AmazeFileManager.apk" "emulator-5554" Android10.0 output2 3600 ./example/example_property.py 1000 random
    
    # 如果不是最后一次运行，则等待
    if [ $run_count -lt $MAX_RUNS ]; then
        echo "等待 $INTERVAL_MINUTES 分钟进行下一次运行..."
        sleep $((INTERVAL_MINUTES * 60))
    fi
done

echo "已完成所有 $MAX_RUNS 次运行"