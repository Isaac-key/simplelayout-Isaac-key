import argparse


def get_options():
    parser = argparse.ArgumentParser()
    # TODO: 按 1-simplelayout-CLI 要求添加相应参数
    parser.add_argument('--board_grid', type=int,
                        help='布局板分辨率，矩形区域的边长像素数')
    parser.add_argument('--unit_grid', type=int,
                        help='矩形组件分辨率')
    parser.add_argument('--unit_n', type=int,
                        help='组件数')
    parser.add_argument('--positions', type=int,
                        nargs='+',
                        help='代表每个组件的位置编号')
    parser.add_argument('-o', '--outdir', type=str,
                        help='输出结果的目录，默认为example_dir',
                        default='example_dir')
    parser.add_argument('--file_name', type=str,
                        help='输出文件名',
                        default='example')
    options = parser.parse_args()
    return options
