library(tidyverse)
library(readr)

# Change this date to match your downloaded file each time
new_run <- read_csv("~/Downloads/SkiSafe Run Mar 20 2026.csv")

# Relative path — works on any machine
master <- read_csv("data/Ski_Safe_Runs.csv")

# Append and deduplicate
master <- bind_rows(master, new_run) %>% distinct()

# Save back
write_csv(master, "data/Ski_Safe_Runs.csv")

