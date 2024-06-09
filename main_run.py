import meteo_de_muy_cold as meteo

#fill the paths to run
result, message, final_file_path = meteo.api_main(r"manual_input\manual_input.yaml",r"C:\Users\...\Meteo")
print(message)
print(result)
print(final_file_path)