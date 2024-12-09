

def server_init(nums, base):
    server_i = {'status': 'пусто',
                'run': '',
                'time_begin_curr': '',
                'time_end_curr': '',
                'stack': []}
    for i in range(nums):
        base[f'Сервер {i+1}'] = server_i


num_servers = int(input('Добро пожаловать в симулятор распределенной системы.\nВведите количество серверов: '))
vir_sys = {}

server_init(num_servers, vir_sys)

print(vir_sys)
'''
server_i = {'name': f'Сервер {i}',
                    'status': 'пусто',
                    'run': '',
                    'time_begin_curr': '',
                    'time_end_curr': '',
                    'stack': []}
'''