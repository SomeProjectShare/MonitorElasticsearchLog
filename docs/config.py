send_dingding_alert_url = "xxx"
level = "ERROR"
head = ["xxx", "xxx", "... ..."]
env = ["dev", "uat", "prod"]
app = [
    "xxx", "xxx", "... ..."
]
elastic_user = "xxx"
elastic_password = "xxx"
elastic_ecs_ip = "xxx"
elastic_ecs_port = "xxx"
database_filename = "MonitorElasticsearchLog.db"
database_table = "{0}_{1}_{2}"
create_database_table = "create table {0} (id int not null, head char(32), env char(9), app char(64), record_time datetime, level char(9), logger_name char(128), es_timestamp varchar(128), message varchar(256));"