
def EnviarCorreo(nombre_entrada,dni_entrada,correo_entrada):
    from email.mime.text import MIMEText
    from smtplib import SMTP
    from datetime import datetime
    nombre = nombre_entrada
    dni = dni_entrada
    correo = correo_entrada
    # obtener fecha actual
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # construir mensaje para el cliente
    mensaje = ("Se deja constancia de recepción del dispositivo a nombre de " + nombre + " con DNI " + dni 
              + " Hoy " + fecha + ". Se le comunicará por correo al cliente cuando el equipo esté listo para retirar."
              + " Transcurridos los 30 días posteriores a este aviso, queda a disposición de la empresa por los artículos 2525/2526."
              + " Todos los arreglos cuentan con una garantía de 3 (tres) meses por falla o mal funcionamiento del repuesto cambiado."
              + " No se gozará de dicha garantía, sin excepción, en los siguientes casos: Equipos mojados o con humedad, rotura del/los repuestos colocados o consumos en la placa en cambios de batería."
              + " Baño Químico: El equipo recibido que tenga muestras de agua o sensores de humedad activados será ingresado como sin funcionamiento."
              + " El cliente debe saber que por más que el equipo ingrese encendido puede llegar a tener inconvenientes al realizarle el lavado químico y quedar sin funcionamiento o con fallas técnicas."
              + " En caso de que el teléfono encienda luego del lavado químico se le cobrará al cliente el monto avisado al momento de dejar el dispositivo."
              + " Arreglo de software: Este trabajo exige un reseteo del equipo por lo que la información del mismo como imágenes, videos y archivos se perderán si el cliente no realiza una copia anticipadamente."
              + " Solo se podrá reclamar garantía por fallas referidas al software y no de hardware.") 
    
    # enviar correo al cliente
    remitente = "toxicaseiphone@gmail.com"
    destinatario = correo
    mensaje_correo = MIMEText(mensaje)
    mensaje_correo["From"] = remitente
    mensaje_correo["To"] = destinatario
    mensaje_correo["Subject"] = "Toxicase recibió tu teléfono"
    servidor = SMTP("smtp.gmail.com", 587)
    servidor.ehlo()
    servidor.starttls()
    servidor.ehlo()
    servidor.login(remitente, "meeatbclrguxzmmg")
    servidor.sendmail(remitente, destinatario, mensaje_correo.as_string())
    servidor.quit()
    print("Correo enviado")
