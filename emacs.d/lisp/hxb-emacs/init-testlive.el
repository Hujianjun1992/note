;;;;;;;;;;;;;;;;;

;auctex

;;;;;;;;;;;;;;;;;



;;把 auctex 加入到 load-path 中，然后加载 auctex 

;;如果 emacs 是运行在多需折腾的 windows 平台上，系统会加载 "tex-mik"

(add-to-list 'load-path

             "~/.emacs.d/auctex/site-lisp/site-start.d");;根据自己的Auctex位置修改目录



(load "auctex.el" nil t t)

;;(load "preview-latex.el" nil t t)          ;;preview-latex.el ..

(if (string-equal system-type "windows-nt")

    (require 'tex-mik))

	

	

;;LaTeX 设置

;;???为 LaTeX 模式 hook，自动换行，数学公式，reftex 和显示行号的功能。

(mapc (lambda (mode)

      (add-hook 'LaTeX-mode-hook mode))

      (list 'auto-fill-mode

            'LaTeX-math-mode

            'turn-on-reftex

            'linum-mode))



;;在 LaTeX mode 中，默认开启 PDF mode，即默认使用 xelatex 直接生成 pdf 文

;;件，而不用每次用 'C-c C-t C-p' 进行切换。设置 'Tex-show-compilation' 为

;;t，在另一个窗口显示编译信息，对于错误的排除很方便。另外，编译时默认直接

;;保存文件，绑定补全符号到 TAB 键。			

(add-hook 'LaTeX-mode-hook

          (lambda ()

		   ;;加载自己喜好的可执行程序【xelatex,pdflatex......】

		   (add-to-list 'TeX-command-list '("XeLaTeX" "%`xelatex%(mode)%' %t" TeX-run-TeX nil t))

		   (add-to-list 'TeX-command-list '("dviout" "%`dviout%(mode)%' %t" TeX-run-TeX nil t))

           (setq TeX-command-default "XeLaTeX")

            (setq TeX-auto-untabify t     ; remove all tabs before saving

                  TeX-engine 'xetex       ; use xelatex default,对中文的支持比较好

                  TeX-show-compilation t) ; display compilation windows

            (TeX-global-PDF-mode t)       ; PDF mode enable, not plain

            (setq TeX-save-query nil)

            (imenu-add-menubar-index)

            (define-key LaTeX-mode-map (kbd "TAB") 'TeX-complete-symbol)))

			

;;还没有添加打开pdf的工具 比如福昕阅读器
