import os
import json
import glob
import shutil
from distutils.dir_util import copy_tree


reports_dir = os.environ['reports_dir']

subfolders = [ f.path for f in os.scandir(reports_dir) if f.is_dir() ]
for folder in subfolders:
    test_name = os.path.basename(folder)
    test_data = {'test-name': test_name}

    print('Export test: {}'.format(test_name))

    # Write test info json
    with open(os.path.join(folder, 'test-info.json'), 'w') as outfile:
        json.dump(test_data, outfile)

    # Find screenshots related to this tests
    for file in glob.glob('./cypress/**/{}*.*'.format(test_name), recursive=True):
        print('Found file: {} - matching test: {}'.format(os.path.basename(file), test_name))
        shutil.copyfile(file, os.path.join(folder, os.path.basename(file)))

    test_results_dir = os.environ['test_results_dir']

    copy_tree(reports_dir, test_results_dir)
