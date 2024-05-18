## LOGICA

# Verander de vergelijkingsoperator zodat de print uitgevoerd wordt

# Voorbeeld:
x = 5
z = 5
#if (z > 4):
  #print(z)
  
#if z == x:
  #print(z)

#if not z + 2 < 3:
  #print(z)

#if z > 3 != 2:
  #print(z)

## STRINGS

#naam    = input('Wat is je naam? ')
#salaris = int(input('Hoeveel heb je deze maand verdiend? '))
#uurloon = int(input('Hoeveel krijg je per uur? '))

# > print nu met 'f'-strings  de naam van deze pesoon, hoeveel deze persoon verdiend heeft, het uurloon en hoeveel uren deze persoon dus gewerkt heeft.
#print(f'Je naam is {naam}, je hebt deze maand {salaris} verdiend en je krijgt {uurloon} per uur')

# > Vraag een gebruiker in welk jaar deze persoon geboren is
#geboortejaar = int(input('In welk jaartal ben je geboren?'))
# > Vraag ook welk jaar het nu is
#huidigJaar = int(input('Welk jaar is het nu?'))
# > Bereken hoe oud deze persoon is, en print zo vaak 'HOERA!' door middel van een f-string
#print('HOERA!' * (huidigJaar - geboortejaar))

# > Vraag een gebruiker om een woord in te typen
#woordInvoer = input('Voer nu een woord in, jij woordslet! ')
# > Vraag de gebruiker ook om een letter in te geven
#letterInvoer = input('Maar één woord? Wat ben je, een watje?! Snel, geef me een extra letter! ')
# > Print of de gegeven letter in het woord voorkomt 
#print(letterInvoer in woordInvoer)

# Maak een super slecht wachtwoord programma.
# > Vraag een gebruiker om een wachtwoord in te stellen
wachtwoord = input('Halt! Wat is het wachtwoord?!')
# > Vraag een gebruiker om het wachtwoord te herhalen
wachtwoordCheck = input('Euh, sorry, wat zei je?')
# > Kijk of deze overeenkomen
if wachtwoord == wachtwoordCheck:
  print('Oké, loop maar door.')
  wachtwoordVariable = wachtwoord
else:
  print('Stop, je hebt de wet overtreden! Je gaat naar de gevangenis, schavuit!')
# > Sla het wachtwoord op in een variabele
