

def server_init(nums, base):
    server_i = {'status': 'пусто',
                'run': '',
                'time_begin_curr': '',
                'time_end_curr': '',
                'stack': []}
    for i in range(nums):
        base[f'Сервер {i+1}'] = server_i


def show_status_serv(base):
    print('Состояние серверов:')
    for serv in base:
        if base[serv]['status'] == 'пусто':
            print(f'{serv}: пусто')
        else:
            print(f'Выполняет задание (осталось {2+2} сек.)')


def show_help():
    print('Команды:\n'
          '"добавить n" - для добавления задания, n - количество секунд.\n'
          '"состояние серверов" - для перехода в режим обработки заданий\n'
          '"выход" - для завершения работы')


num_servers = int(input('Добро пожаловать в симулятор распределенной системы.\nВведите количество серверов: '))
vir_sys = {}

server_init(num_servers, vir_sys)
show_status_serv(vir_sys)
show_help()
while True:
    input_command = input('Команда: ').split()
    if input_command[0] == 'добавить':
        print(f'задание с {input_command[1]} секундами добавлено в очередь')
    elif input_command == ['состояние', 'серверов']:
        print()
        show_status_serv(vir_sys)
        print()
    elif input_command[0] == 'выход':
        print('\nЗавершение работы.')
        break

'''
server_i = {'name': f'Сервер {i}',
                    'status': 'пусто',
                    'run': '',
                    'time_begin_curr': '',
                    'time_end_curr': '',
                    'stack': []}
'''