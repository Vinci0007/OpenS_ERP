#import UsersLogin
#import UsersManage
#import time
#import hashlib


#sessions = {}


#def login(username, password):
#    password_hash = hashlib.sha256(password.encode()).hexdigest()
#    if username in UsersLogin.user_database and UsersLogin.user_database[username] == password_hash:
#        session_id = generate_session_id()
#        sessions[session_id] = {
#            "username": username,
#            "last_activity": time.time()
#        }
#        print("Login successful!")
#        return session_id
#    else:
#        print("Invalid username or password.")
#        return None


#def generate_session_id():
#    # 生成一个唯一的会话 ID
#    return str(hash(time.time()))


#def perform_action(session_id, action):
#    if session_id in sessions:
#        # 更新最后活动时间
#        sessions[session_id]["last_activity"] = time.time()

#        # 检查用户权限
#        username = sessions[session_id]["username"]
#        if UsersManage.check_permission(username, action):
#            # 执行相应的操作
#            print(f"Performing {action} action.")
#    else:
#        print("Invalid session. Please log in again.")


#def logout(session_id):
#    if session_id in sessions:
#        del sessions[session_id]
#        print("Logged out successfully.")
#    else:
#        print("Invalid session.")
