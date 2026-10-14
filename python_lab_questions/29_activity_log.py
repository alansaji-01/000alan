# Append the current date-time and activity to activity.log.
import logging
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
if __name__ == '__main__':
    activity = input('Enter user activity: ')
    logging.info('%s', activity)
    print('Activity recorded in activity.log')
