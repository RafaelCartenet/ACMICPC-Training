import os
import time

IN_EXTENSION = '.in'
OUT_EXTENSION = '.ans'


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
    }
    print('status  | duration  | sample\t')

    output_str = '%s \t\t| %.2fs \t| %s '

    for sample_name, sample in load_all_samples(samples_path):
        input, output = sample
        start = time.time()
        try:
            my_answer = run_function(function, input)
            success = output == my_answer
            success_str = str_mapping[success]
            print(output_str % (
                success_str,
                time.time() - start,
                sample_name,
            ))
        except:
            print(output_str % (
                str_mapping['error'],
                time.time() - start,
                sample_name,
            ))
