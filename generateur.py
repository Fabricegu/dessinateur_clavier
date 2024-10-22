
import svgwrite
import svg2gcode
from PIL import Image
import numpy as np
from matplotlib.font_manager import FontProperties

echelle = 1
board_width_mm = 420
board_height_mm = 210
bord_cut_x = 5
bord_cut_y = 5
marge_X_mm = 5 + bord_cut_x
marge_Y_mm = 5 + bord_cut_y
# Épaisseur de trait en mm
line_width_mm = 1

# Rayon des coins arrondis en mm
corner_radius_mm = 3
taille_police = '50px'

# Nom du fichier SVG de sortie
filename = 'clavier16.svg'

# Charger une police Single Line Font
#police = FontProperties(fname="1CamBam_Stick_0")



SPACE_X = 7 * echelle  # espace horizontal entre les touches
SPACE_Y = 5 * echelle  # espace vertical entres les touches

SIZE_KEY_X = 17 * echelle * 1.4  # largeur de base d'une touche
SIZE_KEY_Y = 20 * echelle * 1  # hauteur de base d'une touche


OFFSET_CADRE_X = 5 * echelle
OFFSET_CADRE_Y = 5 * echelle

POSITION_LIGNE1_X = OFFSET_CADRE_X + SPACE_X


def mm_to_px(mm, dpi):
    inch = mm / 25.4
    px = inch * dpi
    return px


def key_function(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 2
    height_mm = SIZE_KEY_Y
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    milieu_texte_X = x + width_mm/2
    milieu_texte_Y = y + height_mm/2 + 6
    #text = dwg.text(name, insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
    #                text_anchor='middle', font_size=taille_police, font_family='1CamBam_Stick_0C', stroke_width=f"{1}mm", font_weight='100')

    x_text = round(milieu_texte_X*3.776)
    y_text = round(milieu_texte_Y*3.776)
   
    text = dwg.text(name, insert=(x_text, y_text),
                    text_anchor='middle', font_size=taille_police, font_family='Liberation Sans', stroke_width=f"{1}mm", font_weight='100')
         
    #text = dwg.text(name, insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
    #                text_anchor='middle', font_size=taille_police, font_family='Liberation Sans', stroke_width=f"{1}mm", font_weight='100')
      
    dwg.add(text)
    dwg.save()
    return width_mm


def key_letter(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 1

    height_mm = SIZE_KEY_Y
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    milieu_texte_X = x + width_mm/2
    milieu_texte_Y = y + height_mm/2 + 6

    x_text = round(milieu_texte_X*3.776)
    y_text = round(milieu_texte_Y*3.776)
   
    text = dwg.text(name, insert=(x_text, y_text),
                    text_anchor='middle', font_size=taille_police, font_family='Liberation Sans', stroke_width=f"{1}mm", font_weight='100')
     

    #text = dwg.text(name, insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
    #                text_anchor='middle', font_size=taille_police, font_family='1CamBam_Stick_0C')
    dwg.add(text)
    dwg.save()
    return width_mm


def key_arrow_v(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 2
    height_mm = SIZE_KEY_Y

    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    milieu_texte_X = x + width_mm/2
    milieu_texte_Y = y + height_mm/2 + 8
    text = dwg.text(name, insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
                    text_anchor='middle', font_size='80px', font_family='1CamBam_Stick_0C')
    dwg.add(text)
    dwg.save()
    return width_mm


def key_arrow_h_left(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 2
    height_mm = SIZE_KEY_Y


    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    margex = 12
    pointe_fleche_X = x + margex
    pointe_fleche_Y = y + height_mm/2
    debut_fleche_X = x + width_mm - margex
    debut_fleche_Y = y + height_mm/2
    
    arrow_width = 10
    

    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X + arrow_width}mm", f"{pointe_fleche_Y - arrow_width/3}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X + arrow_width}mm", f"{pointe_fleche_Y + arrow_width/3}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{(debut_fleche_X)}mm", f"{debut_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    dwg.save()
    return width_mm
def key_arrow_up(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 2
    height_mm = SIZE_KEY_Y


    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    margex = 12
    margey = 4
    pointe_fleche_X = x + width_mm/2
    pointe_fleche_Y = y + margey
    debut_fleche_X = x + width_mm/2
    debut_fleche_Y = y + height_mm - margey
    
    arrow_width = 6
    

    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                 end=(f"{pointe_fleche_X - arrow_width/2}mm", f"{pointe_fleche_Y + arrow_width}mm"),
                    stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                 end=(f"{pointe_fleche_X + arrow_width/2}mm", f"{pointe_fleche_Y + arrow_width}mm"),
                    stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{(debut_fleche_X)}mm", f"{debut_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    dwg.save()
    return width_mm

def key_arrow_down(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 2
    height_mm = SIZE_KEY_Y


    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    margex = 12
    margey = 4
    debut_fleche_X = x + width_mm/2
    debut_fleche_Y = y + margey
    pointe_fleche_X = x + width_mm/2
    pointe_fleche_Y = y + height_mm - margey
    
    arrow_width = 6
    

    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                 end=(f"{pointe_fleche_X - arrow_width/2}mm", f"{pointe_fleche_Y - arrow_width}mm"),
                    stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                 end=(f"{pointe_fleche_X + arrow_width/2}mm", f"{pointe_fleche_Y - arrow_width}mm"),
                    stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{(debut_fleche_X)}mm", f"{debut_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    dwg.save()
    return width_mm


def key_arrow_h_right(dwg, name, x, y):
    width_mm = SIZE_KEY_X * 2
    height_mm = SIZE_KEY_Y


    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    margex = 12
    debut_fleche_X = x + margex
    debut_fleche_Y = y + height_mm/2
    pointe_fleche_X = x + width_mm - margex
    pointe_fleche_Y = y + height_mm/2
    
    arrow_width = 10
    

    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X - arrow_width}mm", f"{pointe_fleche_Y - arrow_width/3}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X - arrow_width}mm", f"{pointe_fleche_Y + arrow_width/3}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    
    dwg.add(dwg.line(start=(f"{(debut_fleche_X)}mm", f"{debut_fleche_Y}mm"),
                     end=(f"{pointe_fleche_X}mm", f"{pointe_fleche_Y}mm"),
                     stroke='black', stroke_width=f"{line_width_mm}mm"))
    dwg.save()
    return width_mm


def key_enter(dwg, x, y):
    width_mm = SIZE_KEY_X * 2

    height_mm = SIZE_KEY_Y * 2 + SPACE_Y * 1.5
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    milieu_texte_X = x + width_mm/2
    milieu_texte_Y = y + height_mm/2 + 7
    x_text = round(milieu_texte_X*3.776)
    y_text = round(milieu_texte_Y*3.776)
   
    text = dwg.text('OK', insert=(x_text, y_text),
                    text_anchor='middle', font_size='80px', font_family='Liberation Sans', stroke_width=f"{1}mm", font_weight='100')
     
    
    #text = dwg.text('OK', insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
    #                text_anchor='middle', font_size='80px', font_family='1CamBam_Stick_0C')
    dwg.add(text)
    dwg.save()
    return width_mm


def key_delete(dwg, x, y):
    width_mm = SIZE_KEY_X * 2

    height_mm = SIZE_KEY_Y
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    milieu_texte_X = x + width_mm/2
    milieu_texte_Y = y + height_mm/2 + 6
    x_text = round(milieu_texte_X*3.776)
    y_text = round(milieu_texte_Y*3.776)
   
    text = dwg.text('DEL', insert=(x_text, y_text),
                    text_anchor='middle', font_size='50px', font_family='Liberation Sans', stroke_width=f"{1}mm", font_weight='100')
     

    #text = dwg.text('DEL', insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
    #                text_anchor='middle', font_size='50px', font_family='1CamBam_Stick_0C')
    dwg.add(text)
    dwg.save()
    return width_mm


def key_space(dwg, x, y):
    width_mm = SIZE_KEY_X * 7

    height_mm = SIZE_KEY_Y
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    milieu_texte_X = x + width_mm/2
    milieu_texte_Y = y + height_mm/2 + 7

    x_text = round(milieu_texte_X*3.776)
    y_text = round(milieu_texte_Y*3.776)
   
    text = dwg.text('ESPACE', insert=(x_text, y_text),
                    text_anchor='middle', font_size='60px', font_family='Liberation Sans', stroke_width=f"{1}mm", font_weight='100')
     

    #text = dwg.text('ESPACE', insert=((f"{milieu_texte_X}mm"), (f"{milieu_texte_Y}mm")),
    #                text_anchor='middle', font_size='60px', font_family='1CamBam_Stick_0C')
    dwg.add(text)
    # dwg.save()
    return width_mm


def circle(dwg, x, y, radius):
    dwg.add(dwg.circle(center=(f"{x}mm", f"{y}mm"), r=f"{radius}mm",
                       fill='none', stroke='black', stroke_width=f"{line_width_mm}mm"))

    dwg.add(dwg.circle(center=(f"{x}mm", f"{y}mm"), r=f"{1}mm",
                       fill='none', stroke='black', stroke_width=f"{line_width_mm}mm"))


def cadre(dwg, bord_X, bord_Y):

    width_mm = board_width_mm - bord_X * 2
    height_mm = board_height_mm - bord_Y * 2
    x = bord_X + line_width_mm
    y = bord_Y + line_width_mm
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm}mm",
        ry=f"{corner_radius_mm}mm", stroke_width=f"{line_width_mm}mm"))
    dwg.save()


def detourage(dwg, bord_X, bord_Y, end_X, end_Y):

    width_mm = end_X + 1
    height_mm = end_Y + 1
    x = bord_X
    y = bord_Y
    dwg.add(dwg.rect(insert=(f"{x}mm", f"{y}mm"), size=(
        f"{width_mm}mm", f"{height_mm}mm"), fill='none', stroke='black', rx=f"{corner_radius_mm*3}mm",
        ry=f"{corner_radius_mm*3}mm", stroke_width=f"{line_width_mm}mm"))

    cut_x0 = 0
    cut_y0 = 0
    cut_x1 = width_mm + x*2
    cut_y1 = height_mm + y*2
    # dwg.add(dwg.rect(insert=(f"{cut_x0}mm", f"{cut_y0}mm"), size=(
    #    f"{cut_x1}mm", f"{cut_y1}mm"), fill='none', stroke='black', stroke_width=f"{1}mm"))

    dwg.save()
    #print(cut_x1)
    #print(cut_y1)
    print(filename + ' completed')


dwg = svgwrite.Drawing(filename, profile='tiny', size=(
    f"{board_width_mm}mm", f"{board_height_mm}mm"))

# cadre

# cadre(dwg, marge_X_mm, marge_Y_mm)

# ligne 1
x = 8 * SPACE_X + marge_X_mm
y = 2*SPACE_Y + marge_Y_mm
dx = key_function(dwg, 'Acc.', x, y)

x = x + SPACE_X + dx
dx = key_function(dwg, 'Rech.', x, y)


x = x + SPACE_X + dx
dx = key_function(dwg, 'Emp.', x, y)


x = x + SPACE_X + dx
dx = key_function(dwg, 'Bio.', x, y)

x = x + SPACE_X + dx
dx = key_letter(dwg, '-', x, y)

x = x + SPACE_X + dx
dx = key_letter(dwg, '+', x, y)


# ligne 2
liste = ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
x = marge_X_mm
y = y + SPACE_Y + SIZE_KEY_Y + marge_Y_mm
dx = 0
for i in range(len(liste)):
    x = x + SPACE_X + dx
    dx = key_letter(dwg, liste[i], x, y)

x = x + SPACE_X * 2.5 + dx
dx = key_delete(dwg, x, y)


# ligne 3
liste = ['Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M']
x = SPACE_X * 1.5 + marge_X_mm
y = y + SPACE_Y + SIZE_KEY_Y + marge_Y_mm
dx = 0
for i in range(len(liste)):
    x = x + SPACE_X + dx
    dx = key_letter(dwg, liste[i], x, y)
    dwg.save()

x = x + SPACE_X + dx
dx = key_enter(dwg, x, y)

last_x = x + dx

# ligne 4
liste = ['W', 'X', 'C', 'V', 'B', 'N']
x = 0 + marge_X_mm
y = y + SPACE_Y + SIZE_KEY_Y + marge_Y_mm
dx = 0
for i in range(len(liste)):
    x = x + SPACE_X + dx
    dx = key_letter(dwg, liste[i], x, y)
    dwg.save()

x = x + 2*SPACE_X + dx
dx = key_arrow_up(dwg, '\u2191', x, y)

x = x + 2*SPACE_X + dx
dx = key_arrow_down(dwg, '\u2193', x, y)

# ligne 5

x = SPACE_X * 2 + SIZE_KEY_X * 1 + marge_X_mm
y = y + SPACE_Y + SIZE_KEY_Y + marge_Y_mm
dx = key_arrow_h_left(dwg, '\u2190', x, y)

x = x + dx + SPACE_X * 1 + SIZE_KEY_X * 0
dx = key_space(dwg, x, y)

x = x + dx + SPACE_X * 1 + SIZE_KEY_X * 0
dx = key_arrow_h_right(dwg, '\u2192', x, y)

last_y = y + SIZE_KEY_Y

# repere bas
x = x + dx + SPACE_X * 3 + SIZE_KEY_X * 1
y = y + SIZE_KEY_Y/2
circle(dwg, x, y, 10)

# repere haut droit
#x = x + dx + SPACE_X * 2 + SIZE_KEY_X * 1
y = marge_Y_mm + SPACE_Y * 2 + SIZE_KEY_Y/2
circle(dwg, x, y, 10)


# repere haut gauche
x = marge_X_mm + SPACE_X * 0 + SIZE_KEY_X
y = marge_Y_mm + SPACE_Y * 2 + SIZE_KEY_Y/2
circle(dwg, x, y, 10)



detourage(dwg, marge_X_mm, marge_Y_mm,
          (last_x + SPACE_X/2), (last_y + SPACE_Y))

dwg.save()