from pyscript import display, document

def countries_capital(e):
    document.getElementById('output').innerHTML = ''
    user_input = document.getElementById('input1').value.strip()
    
    countries = {
        'Madagascar': 'Antananarivo',
        'Mongolia': 'Ulaanbaatar',
        'Egypt': 'Cairo',
        'Philippines': 'Manila',
        'USA': 'Washington D.C.',
        'Denmark': 'Copenhagen',
        'Chile': 'Santiago'
    }
    
    matched_country = next((k for k in countries if k.lower() == user_input.lower()), None)
    
    if matched_country:
        display(countries[matched_country], target='output')
    else:
        display(f'Sorry, no {user_input} in the list', target='output')