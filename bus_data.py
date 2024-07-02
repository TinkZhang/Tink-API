latestVersion = "2024.07.02"

# trip的属性
# driver: 司机
# plate: 车牌号
# color: 车辆颜色
# directionToHome: 回家True/离家False
# leaveTime: ~8:00 有~表示大约时间
# arriveTime: ~8:00 有~表示大约时间
lines = [
    {
        "lineId": "11",
        "lineDescription": "11号线康新公路",
        "trips": [
            {"driver": "hello", "plate": "HuA23242", "color": "Green", "directionToHome": True, "leaveTime": "8:00",
             "arriveTime": "8:15"},
            {"driver": "hello2", "plate": "HuA2e242", "color": "Green", "directionToHome": True, "leaveTime": "8:00",
             "arriveTime": "8:15"}
        ]
    },
    {
        "lineId": "16",
        "lineDescription": "16号线周浦东",
        "trips": [
            {"driver": "hello", "plate": "HuA23242", "color": "Green", "directionToHome": True, "leaveTime": "8:00",
             "arriveTime": "8:15"},
            {"driver": "hello2", "plate": "HuA2e242", "color": "Green", "directionToHome": True, "leaveTime": "8:00",
             "arriveTime": "8:15"}
        ]
    },
]
