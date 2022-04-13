
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_scraper_count_cnut():
    url = "https://en.wikipedia.org/wiki/Cnut#Statesmanship"
    assert get_citations_needed_count(url) == 6

def test_scraper_passages_cnut():
    url = "https://en.wikipedia.org/wiki/Cnut#Statesmanship"
    
    assert get_citations_needed_report(url).split('\n')[0] == "This initial distribution of power was short-lived. The chronically treacherous Eadric was executed within a year of Cnut's accession.[42] Mercia passed to one of the leading families of the region, probably first to Leofwine, ealdorman of the Hwicce under Æthelred, but certainly soon to his son Leofric.[45] In 1021, Thorkel also fell from favour and was outlawed. Following the death of Erik in the 1020s, he was succeeded as Earl of Northumbria by Siward, whose grandmother,[citation needed] Estrid (married to Úlfr Thorgilsson), was Cnut's sister. Bernicia, the northern part of Northumbria, was theoretically part of Erik and Siward's earldom, but throughout Cnut's reign it effectively remained under the control of the English dynasty based at Bamburgh, which had dominated the area at least since the early 10th century. They served as junior Earls of Bernicia under the titular authority of the Earl of Northumbria. By the 1030s Cnut's direct administration of Wessex had come to an end, with the establishment of an earldom under Godwin, an Englishman from a powerful Sussex family. In general, after initial reliance on his Scandinavian followers in the first years of his reign, Cnut allowed those Anglo-Saxon families of the existing English nobility who had earned his trust to assume rulership of his Earldoms."
    
    assert get_citations_needed_report(url).split('\n')[1] == "Cnut reinstituted the extant laws with a series of proclamations to assuage common grievances brought to his attention, including: On Inheritance in case of Intestacy, and On Heriots and Reliefs.[50] He also strengthened the currency, initiating a series of coins of equal weight to those being used in Denmark and other parts of Scandinavia.[citation needed] He issued the Law codes of Cnut known now as I Cnut and II Cnut, though these seem primarily to have been produced by Wulfstan of York.[51]"
