import bmemcached
import config
import time

if __name__ == '__main__':
    while True:
        mc = bmemcached.Client(config.memcachedURL, config.memcachedUsername, config.memcachedPassword)

        currentState = mc.get('CPULoad')

        print 'Checking state ...'

        if not currentState or (currentState and currentState=='OFF'):
            # sleep for some while here (for #secondsToSleep amount of seconds)
            print 'sleeping for ' + str(config.secondsToSleep) + ' seconds'
            time.sleep(config.secondsToSleep)
        elif currentState and currentState=='ON':
            # create some heavy CPU load (for #secondsToSleep amount of seconds)
            print 'CPU load for ' + str(config.secondsToSleep) + ' seconds'
            startTimeStamp=time.time()
            timediff=0
            while (timediff<int(config.secondsToSleep)):
                a = 2 ** 0.5
                timediff = time.time()-startTimeStamp
                #print timediff



