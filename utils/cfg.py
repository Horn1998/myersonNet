import argparse


################################################################################
# Get parameters from command line
################################################################################

def config_cl():
    # Default message
    parser = argparse.ArgumentParser(
                description= 'Configure the experiment from command line')
                
                
    #####################
    # Auction arguments
    #####################
    #投标人的数量
    parser.add_argument('-agent', '--num_agent', default='6', type=int,\
                            help='Number of agents')
    #竞争物品数量，只能是1
    parser.add_argument('-item', '--num_item', default='1', type=int,\
                            help='Number of items')
    #训练集数量
    parser.add_argument('-sample_train', '--num_sample_train', default='5000', type=int,\
                            help='Number of sampled instances')
    #测试集数量
    parser.add_argument('-sample_test', '--num_sample_test', default='10000', type=int,\
                            help='Number of sampled instances')
    #投标人分布类型
    parser.add_argument('-distr', '--distribution_type', default='uniform', type=str,\
                            help='Distribution of agent valuation.\
                            Must be one of [uniform | asymmetric_uniform\
                            | exponential | irregular' )
    #随机种子
    parser.add_argument('-seed', '--seed_val', default = '3', type=int,\
                            help='Random seed for the initilization of Neural Networks')
                            

    #####################
    # Training arguments
    #####################
                            
    parser.add_argument('-lr', '--learning_rate', default='0.001', type=float,\
                            help='Learning Rate')
                                
    parser.add_argument('-batch', '--batch_size', default='64', type=int,\
                            help='Mini-batch size')

    # parser.add_argument('-iter', '--num_iter', default='500000', type=int,\
    #                         help='Number of iterations of the solver')
    #任务执行轮数
    parser.add_argument('-iter', '--num_iter', default='200000', type=int, \
                        help='Number of iterations of the solver')

    #线性函数的数量
    parser.add_argument('-num_linear', '--num_linear_func', default='10', type=int,\
                            help='Number of linear functions in myersonnet')
    #迈尔森网络最大单元数量
    parser.add_argument('-num_max', '--num_max_units', default='10', type=int,\
                            help='Number of max units in myersonnet')
                            
    parser.add_argument('-skip_iter', '--skip_iter', default='10000', type=int,\
                            help='Number of iteration skipped in Recordings')
                                                                                                          
    args = parser.parse_args()
    
    return args
    
    
    
    
    
    
    
                            