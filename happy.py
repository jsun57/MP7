import os
import argparse
import sys
import ruamel.yaml
yaml = ruamel.yaml.YAML()
yaml.preserve_quotes = True
yaml.explicit_start = True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base', type=str, default='t2m_vq')
    parser.add_argument('--d', type=str, default='date')
    args = parser.parse_args()

    cfg_name = '../cfg/%s.yaml' % args.base
    if not os.path.exists(cfg_name):
        print("Config file doesn't exist: %s" % cfg_name)
        exit(0)
    cfg = yaml.load(open(cfg_name, 'r'))
    os.makedirs('../cfg/%s/' % args.d, exist_ok=True)
    
    vq_type_list = ['rvq', 'fsq']
    enc_dec_type_list = ['conv2d', 'conv']
    num_quantizers_list = [5]
    counter = 0
    for vq_type in vq_type_list:
        for enc_dec_type in enc_dec_type_list:
            for num_quantizers in num_quantizers_list:
                file_name = args.d + '_' + args.base + '_' + vq_type + '_' + enc_dec_type + '_q_' + str(num_quantizers)
                cfg['name'] = file_name
                cfg['vq_name'] = file_name
                cfg['vae_specs']['vq_type'] = vq_type
                cfg['vae_specs']['num_quantizers'] = num_quantizers
                cfg['enc_dec_specs']['enc_dec_type'] = enc_dec_type
                cfg['enc_dec_specs']['light'] = False 
                cfg['enc_dec_specs']['vq_act'] = 'relu' 
                cfg['enc_dec_specs']['vq_norm'] = 'None'
                cfg['learn_specs']['window_size'] = 68
                cfg['learn_specs']['batch_size'] = 200
                cfg['learn_specs']['loss_freq'] = 0
                cfg['learn_specs']['print_iter_log'] = False 
                if vq_type == 'fsq':
                    cfg['vae_specs']['code_dim'] = 4
                with open('../cfg/%s/%s.yaml' % (args.d, file_name), 'w') as file:
                    documents = yaml.dump(cfg, file)
                counter += 1


if __name__ == "__main__":
    main()
