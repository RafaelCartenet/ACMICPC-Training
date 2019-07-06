import os
import time
import signal

IN_EXTENSION = '.in'
OUT_EXTENSION = '.ans'

class TimeoutException(Exception):
    pass

def deadline(timeout, *args):
    """is a the decotator name with the timeout parameter in second"""
    def decorate(f):
        """ the decorator creation """
        def handler(signum, frame):
            """ the handler for the timeout """
            raise TimeoutException() #when the signal have been handle raise the exception

        def new_f(*args):
            """ the initiation of the handler,
            the lauch of the function and the end of it"""
            signal.signal(signal.SIGALRM, handler) #link the SIGALRM signal to the handler
            signal.alarm(timeout) #create an alarm of timeout second
            res = f(*args) #lauch the decorate function with this parameter
            signal.alarm(0) #reinitiate the alarm
            return res #return the return value of the fonction

        new_f.__name__ = f.__name__
        return new_f
    return decorate


def get_all_samples_names(path):
    """
    Get all unique samples for a given directory.
    """
    files = os.listdir(path)
    files_names = map(
        lambda x: x.split('.')[0],
        files
    )
    files_names = list(set(files_names))
    return sorted(files_names)


def load_sample(path, sample_name):
    """
    Load content of a sample (input data and output data) from
    its path and name.
    """
    in_file = path + sample_name + IN_EXTENSION
    out_file = path + sample_name + OUT_EXTENSION

    with open(in_file, 'r') as f:
        in_content = f.read()

    with open(out_file, 'r') as f:
        out_content = f.read()

    return in_content, out_content


def load_all_samples(path):
    """
    Yields samples content, as well as their names, given directory's path
    """
    sample_names = get_all_samples_names(path)
    for sample_name in sample_names:
        yield sample_name, load_sample(
            path=path,
            sample_name=sample_name
        )


@deadline(20)
def run_function(function, input):
    return function(input)


def run_test(samples_path, function):
    """
    Tests the provided function on the samples found in the samples_path
    Handles timeouts
    """
    str_mapping = {
        True: 'OK',
        False: 'KO',
        'error': 'ERR',
        'timeout': 'T-OUT'
    }
    print('status  | sample\t| duration')

    for sample_name, sample in load_all_samples(samples_path):
        input, output = sample
        output_str = '%s\t| %s \t| %.2fs '
        start = time.time()

        try:
            my_answer = run_function(function, input)
            success = output == my_answer
            success_str = str_mapping[success]

            print(output_str % (
                    success_str,
                    sample_name,
                    time.time() - start,
            ))
        except TimeoutException:
            print(output_str % (
                   str_mapping['timeout'],
                    sample_name,
                    time.time() - start,
            ))
        except:
            print(output_str % (
                   str_mapping['error'],
                   sample_name,
                   time.time() - start,
            ))
