chdir /d D:\prontutor\src
SET mydate=%date:~-4,4%%date:~-10,2%%date:~-7,2%


rem set PATH=D:\prontutor\PT3\Lib;D:\prontutor\PT3\Scripts;%PATH%
echo %date% %time% > D:\\daily_updates_output\\oov_analysis\\kok\\log_files\\%mydate%_oov_analysis.txt 2>&1
python analyse_daily_downloads.py D:\\prontutor\\config_files\\daily_updates\\oov_analysis\\config_oov_analysis_kok.xml  D:\\daily_updates_output\\oov_analysis\\kok\\log_files >> D:\\daily_updates_output\\oov_analysis\\kok\\log_files\\%mydate%_oov_analysis.txt 2>&1
echo %date% %time% >> D:\\daily_updates_output\\oov_analysis\\kok\\log_files\\%mydate%_oov_analysis.txt 2>&1
