import argparse


def parse_opt():
    parser = argparse.ArgumentParser()
    # Data input settings
    parser.add_argument(
        '--input_json',
        type=str,
        default='data/videodatainfo_2017.json',
        help='path to the json file containing video info')
    parser.add_argument(
        '--info_json',
        type=str,
        default='data/info.json',
        help='path to the json file containing additional info and vocab')
    parser.add_argument(
        '--caption_json',
        type=str,
        default='data/caption.json',
        help='path to the processed video caption json')

    parser.add_argument(
        '--feats_dir',
        nargs='*',
        type=str,
        default=['data/feats/resnet152/'],
        help='path to the directory containing the preprocessed fc feats')

    parser.add_argument(
        '--spectrogram_dir',
        type=str,
        default='/home/chenxiao/msrvtt_2017/train-video/audio_spectrograms',
        help='path to the directory containing all audio spectrograms in .png format'
    )

    # Model settings
    parser.add_argument(
        "--model", type=str, default='S2VTModel', help="with model to use")

    parser.add_argument(
        "--max_len",
        type=int,
        default=28,
        help='max length of captions(containing <sos>,<eos>)')

    parser.add_argument(
        '--dim_hidden',
        type=int,
        default=512,
        help='size of the rnn hidden layer')

    parser.add_argument(
        '--num_layers', type=int, default=1, help='number of layers in the RNN')

    parser.add_argument(
        '--input_dropout_p',
        type=float,
        default=0.2,
        help='strength of dropout in the Language Model RNN')

    parser.add_argument(
        '--rnn_type', type=str, default='lstm', help='lstm or gru')

    parser.add_argument(
        '--rnn_dropout_p',
        type=float,
        default=0.5,
        help='strength of dropout in the Language Model RNN')

    parser.add_argument(
        '--dim_word',
        type=int,
        default=512,
        help='the encoding size of each token in the vocabulary, and the video.'
    )

    parser.add_argument(
        '--dim_vid',
        type=int,
        default=2048,
        help='dim of features of video frames')

    # Optimization: General

    parser.add_argument(
        '--epochs', type=int, default=6001, help='number of epochs')

    parser.add_argument(
        '--batch_size', type=int, default=128, help='minibatch size')
    parser.add_argument(
        '--grad_clip',
        type=float,
        default=5,  # 5.,
        help='clip gradients at this value')

    parser.add_argument(
        '--self_crit_after',
        type=int,
        default=-1,
        help='After what epoch do we start finetuning the CNN? \
                        (-1 = disable; never finetune, 0 = finetune from start)'
    )

    parser.add_argument(
        '--learning_rate', type=float, default=4e-4, help='learning rate')

    parser.add_argument(
        '--learning_rate_decay_every',
        type=int,
        default=200,
        help='every how many iterations thereafter to drop LR?(in epoch)')
    parser.add_argument('--learning_rate_decay_rate', type=float, default=0.8)
    parser.add_argument(
        '--optim_alpha', type=float, default=0.9, help='alpha for adam')
    parser.add_argument(
        '--optim_beta', type=float, default=0.999, help='beta used for adam')
    parser.add_argument(
        '--optim_epsilon',
        type=float,
        default=1e-8,
        help='epsilon that goes into denominator for smoothing')
    parser.add_argument(
        '--weight_decay',
        type=float,
        default=5e-4,
        help='weight_decay. strength of weight regularization')

    parser.add_argument(
        '--save_checkpoint_every',
        type=int,
        default=50,
        help='how often to save a model checkpoint (in epoch)?')
    parser.add_argument(
        '--checkpoint_path',
        type=str,
        default='save',
        help='directory to store checkpointed models')

    parser.add_argument(
        '--gpu', type=str, default='0', help='gpu device number')
    
    parser.add_argument(
        '--output_dir', type=str, help='output directory of npy'
    )
    args = parser.parse_args()

    return args