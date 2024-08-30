class ApprovalProcess:
    def __init__(self):
        self.states = ['submit', 'save2draft', 'reject', 'reSubmit', 'cancle']
        self.current_state = 'A'
        self.transitions = []

    def add_transition(self, start, end, trigger, action, attributes=None):
        self.transitions.append((start, end, trigger, action, attributes))

    def execute_transition(self, trigger):
        for transition in self.transitions:
            if transition[2] == trigger:
                self.current_state = transition[1]
                transition[3]()
                break
            
    def add_node(self, node):
        pass

def approve():
    print("审批通过")

def reject():
    print("审批拒绝")
    
def rejectAndReSubmit():
    print("审批驳回重新提交")

machine = ApprovalProcess()
machine.add_transition('A', 'B', 'approve', approve)        ##起始状态、目标状态、触发条件、执行的动作和额外属性
machine.add_transition('B', 'C', 'approve', approve)
machine.add_transition('C', 'D', 'approve', approve)
machine.add_transition('D', 'E', 'reject', reject)
machine.execute_transition('approve') # 从 A 状态开始审批流程
