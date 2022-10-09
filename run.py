"""
 * Copyright (C) 2022 run.py by Alexandria Eicher. All Rights Reserved.
 * 
 * This product includes software developed by Alexandria Eicher for 
 * private, personal use. This software is protected by U.S. and international
 * Copyright laws. You may use, distribute and modify this code under the
 * terms of the LICENSE.txt, which can be found in the root directory of 
 * this project (ae-web/LICENSE.txt).
 * 
 * You should have received a copy of LICENSE.txt with this file. 
 * If not, please write to Alexandria Eicher via email at 
 * alexandriaeicher@gmail.com
 """

import sys
# prevents __pycache__ file from being written to commands dir
sys.dont_write_bytecode = True
from os import listdir
import importlib.util

# TODO: add directions to command

class Command:
    def __init__(self, program_name, description, inputs):
        self.filename = None
        self.program_name = program_name
        self.description = description
        self.inputs = inputs

class Input:
    def __init__(self, inputType, name):
        self.inputType = inputType
        self.name = name

# Mechanism for running python commands
class CommandProcessor:
    def __init__(self, commands_dir):
        self.commands = {}
        self.commands_dir = commands_dir
        self.initializeCommands()
    
    def initializeCommands(self):
        count = 1
        # create a Command for each python file in commands_dir
        for f in listdir(commands_dir):
            path_to_file = commands_dir + "/" + f
            this_file = open(path_to_file, "r")
            lines = this_file.readlines()
            command = self.createCommand(lines)
            command.filename = path_to_file
            if (command.description != ""):
                self.commands[str(count)] = command
                count += 1

    def createCommand(self, lines):
        program_name = ""
        description = ""
        input_type = ""
        input_name = ""
        inputs = []
        get_type = False
        get_name = False
        for line in lines:
            if (line.startswith("* end")):
                break
            elif (line.startswith("* program name")):
                program_name = line.split(":")[-1].strip()
            elif (line.startswith("* description")):
                description = line.split(":")[-1].strip()
            elif (line.startswith("* input")):
                get_type = True
            elif get_type:
                get_type = False
                get_name = True
                input_type = line.split(":")[-1].strip()
            elif get_name:
                get_name = False
                input_name = line.split(":")[-1].strip()
                inputs.append(Input(input_type, input_name))
        return Command(program_name, description, inputs)

    def showCommandOptions(self):
        print("Command Processor Usage")
        print("  list               list the available commands")
        print("  run <command #>    run the command associated with #")
        print("  exit               exit the Command Processor")
        print("  help               shows the usage notes")

    def listCommands(self):
        for command in self.commands:
            print(str(command) + ". " + self.commands[command].program_name)
    
    def configureCommand(self, command_num):
        command = self.commands[command_num]
        args = {}
        for arg in command.inputs:
            args[arg.name] = input(arg.name + " >> ")
        self.runCommand(command.filename, args)
        if (input("Run " + command.program_name + " again? (Y/N) >> ").lower() == "y"):
            self.configureCommand(command_num)
        else:
            self.processInput()

    def runCommand(self, filename, args):
        spec = importlib.util.spec_from_file_location(filename[10:-3], filename)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        solution = module.Solution()
        result = solution.run(args)
        print("Result: " + result)

    def processInput(self):
        command = input("Command Processor >>> ")
        if (command.strip() == "list"):
            self.listCommands()
            self.processInput()
        elif (command.startswith("run")):
            command_num = command.split(" ")[-1].strip()
            self.configureCommand(command_num)
        elif (command.strip() == "exit"):
            quit()
        elif (command.strip() == "help"):
            self.showCommandOptions()
            self.processInput()
        else:
            print("Command not found: " + command)
            self.processInput()

if __name__ == "__main__":
    commands_dir = "./commands"
    commandProcessor = CommandProcessor(commands_dir)
    commandProcessor.showCommandOptions()
    commandProcessor.processInput()
