# import os
# pospath = {'data':'Diffusion/data/data.nii.gz',
#            'T1w':'T1w/T1w_acpc_dc_restore_brain1.25.nii.gz',
#            'bvecs':'Diffusion/data/bvecs',
#            'bvals':'Diffusion/data/bvals',
#             'mask':'Diffusion/data/nodif_brain_mask.nii.gz'
#         }
# data_path = os.path.join('100206',pospath['T1w'])
# print(data_path)

#-----------------------------------
# cmd = 'mmrsda {} sakjd {} asd '
#
# print(cmd.format('test1','test2'))

prompt = '\nTell me something, and I will repeat it back to you: '
prompt += '\nEnter quit to end the program.'
message = ''
while message != 'quit':
    message = input(prompt)
    print(message)

