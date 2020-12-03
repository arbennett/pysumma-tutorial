#!/usr/bin/env python
# coding: utf-8

# # A. Explore file manger of SUMMA 3.0.0

# SUMMA has a large number of input files that configure the model and provide the necessary initial conditions and time-varying boundary conditions to make a model simulation. This can at times be confusing. We encourage the user to look at the SUMMA test cases, which provide working SUMMA setups.

# The **`master configuration file`** (called **`file manger`**) is an **ASCII file** and is provided to SUMMA at run-time as a command-line option. The path to this file needs to be supplied with the **`-m`** or **`--master`** command-line flag. The contents of this file orchestrate the remainder of the SUMMA run and are processed by the code in **`build/source/hookup/summaFileManager.f90`**. The file contents mostly consist of file paths that provide the actual information about the model configuration.
# 
# The following items must be provided in order in the master configuration file. Each item must be on its own line, but may be followed by a comment and you can add lines of comments between the items. Each entry must be enclosed in single quotes 'entry'. In the following, I start each enumerated entry with the actual variable name that is used in the SUMMA source code to refer to each of the entries (in summaFileManager.f90) and its default value in case you are trying to trace a problem.
# 
# The model file manager file must also contain the start (`simStartTime`) and end (`simEndTime`) times of the simulation. These are specified as `'YYYY-MM-DD hh:mm'` and must be enclosed in single quotes. They are typically the first model file manager to be specified.

# * `controlVersion`
# : Version of the file manager that should be used to process the master configuration file. At this time, this string should be equal to 'SUMMA_FILE_MANAGER_V3.0'.
# 
# * `simStartTime`: 
# 
# * `simEndTime`: 
# 
# * `tmZoneInfo`: 
# 
# * `settingsPath`: Base path for the configuration files. Most of the file paths in the remainder of the master configuration file are relative to this path (except INPUT_PATH and OUTPUT_PATH).
# 
# * `forcingPath`: Base path for the meteorological forcing files specified in the FORCING_FILELIST.
# 
# * `outputPath`: Base path for the SUMMA output files.
# 
# * `decisionsFile`: File path for the model decisions file (relative to settings_path).
# 
# * `outputControlFile`: File path for the output control file (relative to settings_path).
# 
# * `globalHruParamFile`: File path for the local parameters file (relative to settings_path).
# 
# * `globalGruParamFile`: File path for the basin parameters file (relative to settings_path)'.
# 
# * `attributeFile`: File path for the local attributes file (relative to settings_path).
# 
# * `trialParamFile`: File path for the trial parameters file (relative to settings_path).
# 
# * `forcingListFile`: File path for the list of forcing files file (relative to settings_path).
# 
# * `initConditionFile`: File path for the initial conditions file (relative to settings_path).
# 
# * `outFilePrefix`: Text string prepended to each output filename to identify a specific model setup. Note that the user can further modify the output file name at run-time by using the -s|--suffix command-line option.
# 
# * `vegTableFile`: 
# 
# * `soilTableFile`: 
# 
# * `generalTableFile`:
# 
# * `noahmpTableFile`:

# In[1]:


from pysumma import hydroshare_utils
import os

# Download SUMMA Model Instance from HydroShare
resource_id = '13d6b84a9553410297a67fa366a56cb2'
instance = hydroshare_utils.get_hs_resource(resource_id, os.getcwd())


# In[2]:


get_ipython().system('cd {instance}/; chmod +x ./installTestCases_local.sh')
get_ipython().system('cd {instance}/; ./installTestCases_local.sh')


# ## 1. Import pySUMMA 3.0.0

# In[3]:


import pysumma as ps
import os


# ## 2. Create Simulatioin Object

# In[4]:


instance = 'SummaModel_ReynoldsAspenStand_StomatalResistance'
executable = "/usr/bin/summa.exe"
file_manager = os.path.join(os.getcwd(), instance, 'settings/summa_fileManager_riparianAspenSimpleResistance.txt')

s = ps.Simulation(executable, file_manager)


# ## 3. Explore file manager

# ### 3.1 Show file manager using `orginal_contents` attribute

# In[5]:


s.manager.original_contents


# ### 3.2 Show file manager using `print` command

# In[6]:


print(s.manager)


# ### 3.3 Get value of each line in file manager

# In[7]:


s.manager['settingsPath'].value


# In[8]:


s.manager['forcingPath'].value


# In[9]:


s.manager['attributeFile'].value


# ### 3.4 Change the value of each line in file manager

# In[10]:


# show the current value of simStartTime
s.manager['simStartTime'].value


# In[11]:


# set different value of simStartTime
s.manager['simStartTime'].value = '[notUsed]'


# In[12]:


s.manager['simStartTime'].value


# In[13]:


# another way to set different value of simStartTime
s.manager['simStartTime'].value = '2006-07-01 00:00'


# In[14]:


s.manager['simStartTime'].value


# In[15]:


# overwirte the current value of meta_time in file manger
s.manager.write()


# In[16]:


# check the changed value of meta_time in file manger
print(s.manager)


# ### 3.5 Look at other configuration files using manager modules

# In[17]:


# Read decision text file
print(s.decisions)


# In[18]:


# Read output control text file
print(s.output_control)


# In[19]:


# Read local param info text file
print(s.global_hru_params)


# In[20]:


# Read basin param info text file
print(s.global_gru_params)


# In[21]:


# Read forcing file list
print(s.force_file_list)


# In[22]:


# Read local attributes netCDF file
print(s.local_attributes)


# In[23]:


# Read parameter trial netCDF file
print(s.trial_params)


# In[24]:


# Read parameter trial netCDF file
print(s.initial_conditions)


# In[25]:


for genparm in s.genparm:
    print(genparm.splitlines()[0])


# In[26]:


for mptable in s.mptable:
    print(mptable.splitlines()[0])


# In[27]:


for soilparm in s.soilparm:
    print(soilparm.splitlines()[0])


# In[28]:


for vegparm in s.vegparm:
    print(vegparm.splitlines()[0])


# In[ ]:




