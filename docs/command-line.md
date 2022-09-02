# Kagsa Command Line
in this document you will get all command line usages
```
kagsa [run:<filename>]
      [lib:-l <filename> -o <output>]
	  [version: -v --version]
	  [updates: -u --updates]
	  [help: -h --help]
```
you can use `kg` or `kagsa` for call kagsa in your terminal.

## Run
this is for run a kagsa file, file is must end with `.kg`
```
kagsa file.kg
```

## Build a Library
this used to create library from `.kg` file

you will learn how to write a library later

- `-l` : library
    - this is the input file
    - must end with `.kg`
    - **required**

- `-o` : output
    - this is the output file
    - must end with `.kgl`
    - **required**

```
kagsa -l file.kg -o file.kgl
```

KGL files is a kagsa library extention

## Version
this will give you the current kagsa version
```
kagsa -v
kagsa --version
```

## Updates
this will check if there a new updates on github
```
kagsa -u
kagsa --updates
```

## Help
this will print help message
```
kagsa -h
kagsa --help
```

## Console
if you call kagsa without any argvs this will take you to a kagsa console, write your codes one by one.
```
kagsa
```