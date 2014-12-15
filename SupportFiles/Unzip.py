#------------------------------------------------------------------------------
# Copyright 2014 Esri
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#==============================================================================
#Name:          Unzip.py
#
#Purpose:       Extracts files/folder from zip file.
#
#==============================================================================
import zipfile
import os, sys, traceback

scriptName = sys.argv[0]

# ---------------------------------------------------------------------
# Check arguments
# ---------------------------------------------------------------------   
if len(sys.argv) <> 3:
    print "\n" + scriptName + " <Zip_File_Path> <Unzip_Path>"
    print "\nWhere:"
    print "\n\t<Zip_File_Path> (required parameter) is the path to the zip"
    print "\t\tfile to extract."
    print
    print "\n\t<Unzip_Path> (required parameter) is the path to extract location."
    print
    sys.exit(1)

zipFilePath = sys.argv[1]
extractLocation = sys.argv[2]

if not os.path.exists(zipFilePath):
    print
    print "Zip file " + zipFilePath + " does not exist."
    sys.exit(1)
    
if not os.path.exists(extractLocation):
    print
    print "Unzip path " + extractLocation + " does not exist."
    sys.exit(1)


try:
    
    # -----------------------------------------------------------------------
    # Extract Zip File
    # -----------------------------------------------------------------------
    print ""
    print "--Extracting from zip file: " + zipFilePath
    print "\tto " + extractLocation + \
          "\t(this may take a few minutes)..."
    
    myZipFile = zipfile.ZipFile(zipFilePath)
    myZipFile.extractall(extractLocation)
    
    print "\tDone."

except:
    success = False
    
    # Get the traceback object
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
 
    # Concatenate information together concerning the error into a message string
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError Info:\n" + str(sys.exc_info()[1])
 
    # Print Python error messages for use in Python / Python Window
    print
    print "***** ERROR ENCOUNTERED *****"
    print pymsg + "\n"