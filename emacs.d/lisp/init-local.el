;; -----------------------------------------------------------------------------
;; setting font for mac system
;; -----------------------------------------------------------------------------
;; Setting English Font
(when *is-a-mac*
  (set-face-attribute 'default nil :font "Monaco 16")                  ;;  ;; ;;
  )
;;                                                                       ;; ;;
;; Chinese Font 配制中文字体                                          ;; ;; ;;
(dolist (charset '(kana han symbol cjk-misc bopomofo))                ;; ;; ;;
  (set-fontset-font (frame-parameter nil 'font)                       ;; ;; ;;
                    charset                                           ;; ;; ;;
                    (font-spec :family "Microsoft YaHei" :size 16)))  ;; ;;        ;;
;; Note: you can chang "Kaiti SC" to "Microsoft YaHei" or other fonts ;; ;; ;;

(set-face-attribute 'default nil :height 220)


;;(global-set-key "\d" 'delete-char)
(global-set-key "\C-h" 'backward-delete-char-untabify)
(global-set-key (kbd "¥") "\\") 
(setq ring-bell-function 'ignore)

;;hujianjun

(add-to-list 'load-path (expand-file-name "lisp/hxb-emacs" user-emacs-directory))
(sanityinc/add-subdirs-to-load-path (expand-file-name "lisp/hxb-emacs/" user-emacs-directory))

(require 'cmake-mode)
;;(require 'base)
;;(require 'setnu)
;;(require 'rect-mark)
;;hujianjun



;;(setq load-path (cons (expand-file-name "./cmake-mode") load-path))
;;(require 'cmake-mode)


(add-to-list 'load-path (expand-file-name "lisp/wylin-emacs" user-emacs-directory))
(sanityinc/add-subdirs-to-load-path (expand-file-name "lisp/wylin-emacs/" user-emacs-directory))




;; yasnippet
(require 'init-yasnippet)
(require 'init-ctags)
(require 'init-doxygen)
(require 'init-auctex)
;;(require 'init-science)
(require 'init-wylin-auto-complete)
(require 'init-wylin-cc-auto-complete)

(provide 'init-local)
