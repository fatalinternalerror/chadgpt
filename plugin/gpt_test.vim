if !has('python3')
    echomsg ':python3 is not available, vim-find-test will not be loaded.'
    finish
endif

python3 import gpt.main
python3 object = gpt.main.Main()


command! -nargs=1 GPT3Ask python3 object.ask_gpt3_vim(<f-args>)

