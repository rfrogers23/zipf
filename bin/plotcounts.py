"""Plot wordcounts."""

import argparse
import pandas as pd


def file_wrangler(filepath):
    '''Opens the CSV and returns DataFrame with rank.'''
    # input_csv = args.infile
    df = pd.read_csv(filepath, header=None,
                     names=('word', 'word_frequency'))
    df['rank'] = df['word_frequency'].rank(ascending=False,
                                           method='max')
    df['inverse_rank'] = 1 / df['rank']
    return df
    
def main(args):
    # read CSV file
    df = file_wrangler(args.infile)
    # plot inverse rank
    # save figure using default or specified filename
    scatplot = df.plot.scatter(x='word_frequency',
                               y='inverse_rank',
                               figsize=[12, 6],
                               grid=True,
                               xlim=args.xlim)
    fig = scatplot.get_figure()
    fig.savefig(args.outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('--outfile', type=str,
                        default='plotcounts.png',
                        help="Output file name")
    parser.add_argument('--xlim', type=float, nargs=2, 
                        default=None,
                        metavar=('XMIN','XMAX'), 
                        help='X-axis limits')
    args = parser.parse_args()
    main(args)


