# # 用户会话任务
# def user_session_task(auth_token, user_id):
#     with DBConnection(auth_token) as db_conn:
#         result = db_conn.query(user_id)
#         # 处理查询结果